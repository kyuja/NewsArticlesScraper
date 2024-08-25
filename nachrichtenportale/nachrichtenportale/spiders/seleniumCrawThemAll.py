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
from tldextract import tldextract

from ..items import PortalItem


def get_domain(url):
    url = tldextract.extract(url)
    if 'www' in url.subdomain or url.subdomain == '':
        return url.domain
    else:
        return url.subdomain


class SeleniumCrawlThemAllSpider(Spider):
    name = "seleniumCrawlThemAll"
    homepage_selector = ''
    article_selector = ''
    output_dir = ''
    output_file = datetime.now().strftime("%Y-%m-%d") + '.csv'

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
        time.sleep(5)
        html = self.driver.page_source
        response_obj = HtmlResponse(url=self.driver.current_url, body=html, encoding='utf-8')

        main = response_obj.css(self.homepage_selector)
        urls = main.css('a::attr(href)').getall()

        self.logger.info('Found %i URLs on page %s', len(urls), response.url)
        for link in urls:
            if not link.startswith('https://'):
                link = urljoin(response.url, link)
            yield response.follow(link, self.parse_item)

    def parse_item(self, response):
        self.logger.info("Item function called on %s", response.url)
        self.driver.get(response.url)
        time.sleep(5)
        html = self.driver.page_source
        response = HtmlResponse(url=self.driver.current_url, body=html, encoding='utf-8')
        page_source = self.driver.page_source
        selector = Selector(text=page_source)
        loader = ItemLoader(item=PortalItem(), response=response, selector=selector)
        loader.add_value('portal', get_domain(response.url))
        loader.add_value('today', datetime.now().strftime('%d.%m.%Y %H:%M:%S'))
        loader.add_value('url', response.url)
        loader.add_css('title', 'title::text', TakeFirst())
        loader.add_css('keywords', 'meta[name="keywords"]::attr(content)', TakeFirst())
        loader.add_css('text', self.article_selector, Join())
        loader.add_css('date', 'meta[name="date"]::attr(content)', TakeFirst())
        yield loader.load_item()

    def closed(self, reason):
        self.driver.quit()
