import time
from datetime import datetime
from urllib.parse import urljoin
from itemloaders import ItemLoader
from itemloaders.processors import Join, TakeFirst
from scrapy import Selector
from scrapy import Spider
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from scrapy import Request

from ..items import PortalItem
from ..helpers import get_domain, check_url


class SeleniumCrawlThemAllSpider(Spider):
    name = "seleniumCrawlThemAll"
    homepage_selector = ''
    article_selector = ''
    output_dir = ''
    output_file = datetime.now().strftime("%Y-%m-%d") + '.csv'
    processed_urls = 0
    urls_count = 0

    def __init__(self, portal_csv=None, *args, **kwargs):
        super(SeleniumCrawlThemAllSpider, self).__init__(*args, **kwargs)
        self.start_urls = [portal_csv.get_url()]
        self.allowed_domains = [portal_csv.get_allowed_domain()]
        self.homepage_selector = portal_csv.get_homepage()
        self.article_selector = portal_csv.get_article()
        self.output_dir = get_domain(self.start_urls[0])
        chrome_options = Options()
        self.driver = webdriver.Chrome(options=chrome_options)

    def parse(self, response):
        self.logger.info("Parse function called on %s, with selectors %s and %s", self.start_urls[0],
                         self.homepage_selector, self.article_selector)
        self.driver.get(response.url)
        time.sleep(2)

        self.click_button()

        html = self.driver.page_source
        response_obj = HtmlResponse(url=self.driver.current_url, body=html, encoding='utf-8')
        urls = self.get_urls(response_obj)

        for link in urls:
            if not link.startswith('https://'):
                link = urljoin(response.url, link)
            yield Request(link, callback=self.parse_item)

    def parse_item(self, response):
        self.logger.info("Item function called on %s", response.url)
        self.driver.get(response.url)
        time.sleep(3)

        html = self.driver.page_source
        response = HtmlResponse(url=self.driver.current_url, body=html, encoding='utf-8')
        item = self.load_item(response)
        self.print_progress(response)
        yield item

    def click_button(self):
        from selenium.common import NoSuchElementException
        try:
            iframe = self.driver.find_element(By.XPATH, "//iframe[@title='SP Consent Message']")
            self.driver.switch_to.frame(iframe)
            accept_button = self.driver.find_element(By.XPATH, "//button[@title='Zustimmen und weiter']")
            if accept_button:
                accept_button.click()
                self.logger.info("Button clicked")
                time.sleep(5)
        except NoSuchElementException as e:
            self.logger.info("Button not found")
        finally:
            self.driver.switch_to.default_content()

    def get_urls(self, response_obj):
        main = response_obj.css(self.homepage_selector)
        urls = main.css('a::attr(href)').getall()
        urls = [link for link in urls if check_url(link)]
        self.urls_count = len(urls)
        self.logger.info('Found %i URLs on page %s', self.urls_count, self.start_urls[0])
        return urls

    def print_progress(self, response):
        self.processed_urls += 1
        if self.processed_urls in range(10, self.urls_count, 10):
            print(f'{get_domain(response.url)} Progress: {self.processed_urls}/{self.urls_count}')

    def load_item(self, response):
        page_source = self.driver.page_source
        selector = Selector(text=page_source)

        loader = ItemLoader(item=PortalItem(), response=response, selector=selector)
        loader.add_value('portal', get_domain(response.url))
        loader.add_value('today', datetime.now().strftime('%d.%m.%Y %H:%M:%S'))
        loader.add_value('url', response.url)
        loader.add_css('title', 'title::text', TakeFirst())
        loader.add_css('keywords', 'meta[name="keywords"]::attr(content)', TakeFirst())
        loader.add_css('text', self.article_selector, Join())
        loader.add_css('date',
                       'meta[name="date"]::attr(content), meta[property="article:published_time"]::attr(content)',
                       TakeFirst())

        return loader.load_item()
