from datetime import datetime
import tldextract

import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, Join

from ..items import PortalItem


def get_domain(url):
    url = tldextract.extract(url)
    if url.subdomain == 'www' or url.subdomain == '':
        return url.domain
    else:
        return url.subdomain


class GonnacrawlthemallSpider(scrapy.Spider):
    name = "gonnaCrawlThemAll"
    homepage_selector = ''
    article_selector = ''
    output_dir = ''
    output_file = str(datetime.now().date()) + '.csv'

    def __init__(self, portal_csv=None, *args, **kwargs):
        super(GonnacrawlthemallSpider, self).__init__(*args, **kwargs)
        self.start_urls = [portal_csv.get_url()]
        self.allowed_domains = [portal_csv.get_allowed_domain()]
        self.homepage_selector = portal_csv.get_homepage()
        self.article_selector = portal_csv.get_article()
        self.output_dir = get_domain(self.start_urls[0])

    def parse(self, response):
        self.logger.info("Parse function called on %s, with selectors %s and %s", self.start_urls,
                         self.homepage_selector, self.article_selector)
        main = response.css(self.homepage_selector)
        urls = main.css('a::attr(href)').getall()
        self.logger.info('Found %i URLs from homepage', len(urls))
        for link in urls:
            if not link.startswith('https://'):
                link = response.urljoin(link)
            return Request(link, callback=self.parse_item)

    def parse_item(self, response):
        self.logger.info("Item function called on %s", response.url)
        loader = ItemLoader(item=PortalItem(), response=response)
        loader.add_value('portal', get_domain(response.url))
        loader.add_value('today', str(datetime.now()))
        loader.add_value('url', response.url)
        loader.add_css('title', 'title::text', TakeFirst())
        loader.add_css('keywords', 'meta[name="keywords"]::attr(content)')
        loader.add_css('text', self.article_selector + ' p *::text', Join(separator=' '))
        loader.add_css('date', 'meta[name="date"]::attr(content)')

        yield loader.load_item()
