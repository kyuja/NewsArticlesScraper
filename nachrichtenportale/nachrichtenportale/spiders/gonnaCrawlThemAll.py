import scrapy
from scrapy import Request
from scrapy.spiders import CSVFeedSpider, Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from datetime import datetime

from .. import items


class GonnacrawlthemallSpider(scrapy.Spider):
    name = "gonnaCrawlThemAll"
    allowed_domains = ["tagesschau.de", "zeit.de"]
    start_urls = ["https://tagesschau.de", "https://zeit.de"]

    def parse(self, response):
        self.logger.info("Parse function called on %s", response.url)
        main = response.xpath('//main')
        urls = main.xpath('.//a/@href').get()
        # for link in urls:
        print(response.urljoin(urls))
        return Request(response.urljoin(urls), callback=self.parse_item(response))

    def parse_item(self, response):
        self.logger.info("Item function called on %s", response.url)
        item = items.NachrichtenportalItem()
        item['portal'] = "Tagesschau.de"
        item['today'] = str(datetime.now())
        item["nachricht_url"] = response.url
        item["nachricht_title"] = response.xpath('//title/text()').get()
        item['nachricht_keywords'] = response.xpath('//meta[@name="keywords"]/@content').get()
        item['nachricht_text'] = response.xpath('//article').get()
        item['nachricht_date'] = response.xpath('//meta[@name="date"]/@content').get()
        item['nachricht_extern_links'] = "LINKS"  # response.xpath('')
        print(item.items())
