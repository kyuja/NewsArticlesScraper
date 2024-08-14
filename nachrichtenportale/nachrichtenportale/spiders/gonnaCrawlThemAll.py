from datetime import datetime

import scrapy
from scrapy import Request

from ..import items
from ..helper_functions import get_domain


class GonnacrawlthemallSpider(scrapy.Spider):
    name = "gonnaCrawlThemAll"
    homepage_selector = ''
    article_selector = ''

    def __init__(self, portal=None, *args, **kwargs):
        super(GonnacrawlthemallSpider, self).__init__(*args, **kwargs)
        self.start_urls = [portal.get_url()]
        self.allowed_domains = [portal.get_allowed_domain()]
        self.homepage_selector = portal.get_homepage()
        self.article_selector = portal.get_article()

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
        item = items.NachrichtenportalItem()
        item['portal'] = get_domain(response)
        item['today'] = str(datetime.now())
        item["nachricht_url"] = response.url
        item["nachricht_title"] = response.css('title::text').get()
        item['nachricht_keywords'] = response.css('meta[name="keywords"]::attr(content)').get()
        item['nachricht_text'] = response.css(self.article_selector).getall()
        item['nachricht_date'] = response.css('meta[name="date"]::attr(content)')
