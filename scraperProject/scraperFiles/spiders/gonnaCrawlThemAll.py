from datetime import datetime
import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, Join

from ..items import PortalItem
from ..helpers import get_domain, check_url


class GonnacrawlthemallSpider(scrapy.Spider):
    name = "gonnaCrawlThemAll"
    homepage_selector = ''
    article_selector = ''
    output_dir = ''
    output_file = datetime.now().strftime("%Y-%m-%d") + '.csv'
    processed_urls = 0
    urls_count = 0

    def __init__(self, portal_csv=None, *args, **kwargs):
        super(GonnacrawlthemallSpider, self).__init__(*args, **kwargs)
        self.start_urls = [portal_csv.get_url()]
        self.allowed_domains = [portal_csv.get_allowed_domain()]
        self.homepage_selector = portal_csv.get_homepage()
        self.article_selector = portal_csv.get_article()
        self.output_dir = get_domain(self.start_urls[0])

    def start_requests(self):
        for url in self.start_urls:
            cookies = self.set_cookies(url)
            yield Request(url=url, callback=self.parse, cookies=cookies)

    def parse(self, response):
        self.logger.info("Parse function called on %s, with selectors %s and %s", self.start_urls[0],
                         self.homepage_selector, self.article_selector)

        urls = self.get_urls(response)

        for link in urls:
            if not link.startswith('https://'):
                link = response.urljoin(link)
            yield Request(link, callback=self.parse_item)

    def parse_item(self, response):
        self.logger.info("Item function called on %s", response.url)
        item = self.load_item(response)
        self.print_progress(response)
        yield item

    def print_progress(self, response):
        self.processed_urls += 1
        if self.processed_urls in range(10, self.urls_count, 10):
            print(f'{get_domain(response.url)} Progress: {self.processed_urls}/{self.urls_count}')

    def set_cookies(self, url):
        if 'wiwo' in url:
            cookies = {
                'consentUUID': '9d8641a0-e1aa-4102-8cde-f22e332ccf8b_35',
                'consentDate': '2024-08-24T02:34:47.084Z'
            }
        else:
            cookies = {}
        return cookies

    def get_urls(self, response):
        main = response.css(self.homepage_selector)
        urls = main.css('a::attr(href)').getall()
        urls = [link for link in urls if check_url(link)]
        self.urls_count = len(urls)
        self.logger.info('Found %i URLs on page %s', self.urls_count, self.start_urls[0])
        return urls

    def load_item(self, response):
        loader = ItemLoader(item=PortalItem(), response=response)
        loader.add_value('portal', get_domain(response.url))
        loader.add_value('today', datetime.now().strftime('%d.%m.%Y %H:%M:%S'))
        loader.add_value('url', response.url)
        loader.add_css('title', 'title::text', TakeFirst())
        loader.add_css('keywords', 'meta[name="keywords"]::attr(content)')
        loader.add_css('text', self.article_selector, Join())
        loader.add_css('date', 'meta[name="date"]::attr(content), time::attr(datetime)')

        return loader.load_item()

