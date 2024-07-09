import scrapy
from scrapy import Request
from urllib.parse import urlparse
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from datetime import datetime

from .. import items


def get_domain(response):
    parsed_uri = urlparse(response.url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain


def get_text(response):
    text = response.xpath('//article//text()').getall()
    text = ' '.join(text).strip()
    return text


class GonnacrawlthemallSpider(scrapy.Spider):
    name = "gonnaCrawlThemAll"
    allowed_domains = ["tagesschau.de"]
    start_urls = ["https://tagesschau.de"]

    def parse(self, response):
        self.logger.info("Parse function called on %s", response.url)
        main = response.xpath('//main')
        urls = main.xpath('.//a/@href').getall()
        for link in urls:
            if not link.startswith('https://'):
                link = response.urljoin(link)
            print(link)
            return Request(link, callback=self.parse_item)

    def parse_item(self, response):
        self.logger.info("Item function called on %s", response.url)
        item = items.NachrichtenportalItem()
        item['portal'] = get_domain(response)
        item['today'] = str(datetime.now())
        item["nachricht_url"] = response.url
        item["nachricht_title"] = response.xpath('//title/text()').get()
        item['nachricht_keywords'] = response.xpath('//meta[@name="keywords"]/@content').get()
        item['nachricht_text'] = get_text(response)  # response.xpath('//article').get()
        item['nachricht_date'] = response.xpath('//meta[@name="date"]/@content').get()
        # item['nachricht_extern_links'] = "LINKS"  # response.xpath('')
        print(item.items())
