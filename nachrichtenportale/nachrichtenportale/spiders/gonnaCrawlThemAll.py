import csv
import scrapy
from scrapy import Request
from urllib.parse import urlparse
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from datetime import datetime

from .. import items
from ..portal import Portal


def get_domain(response):
    parsed_uri = urlparse(response.url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain


def get_text(response):
    text = response.xpath('//article//text()').getall()
    text = ' '.join(text).strip()
    return text


def read_csv():
    portale = list()
    with open('../nachrichtenportale/nachrichtenportale/data/Portale.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            portal = Portal(row['start_url'], row['allowed_domains'], row['homepage'], row['article'])
            portale.append(portal)
    return portale


class GonnacrawlthemallSpider(scrapy.Spider):
    name = "gonnaCrawlThemAll"
    allowed_domains = []
    start_urls = []

    def start_requests(self):
        portale = read_csv()
        for portal in portale:
            self.allowed_domains = portal.get_domain()
            self.start_urls = portal.get_url()
            data = {'homepage': portal.get_homepage(), 'article': portal.get_article()}
            print(self.start_urls)
            print(data)
            yield Request(self.start_urls, callback=self.parse, cb_kwargs=data)

    def parse(self, response, **kwargs):
        print(self.start_urls)
        #print(str(**kwargs))

    # def parse(self, response):
    #     self.logger.info("Parse function called on %s", response.url)
    #     main = response.xpath('//main')
    #     urls = main.xpath('.//a/@href').getall()
    #     for link in urls:
    #         if not link.startswith('https://'):
    #             link = response.urljoin(link)
    #         print(link)
    #         return Request(link, callback=self.parse_item)

    # def parse_item(self, response):
    #     self.logger.info("Item function called on %s", response.url)
    #     item = items.NachrichtenportalItem()
    #     item['portal'] = get_domain(response)
    #     item['today'] = str(datetime.now())
    #     item["nachricht_url"] = response.url
    #     item["nachricht_title"] = response.xpath('//title/text()').get()
    #     item['nachricht_keywords'] = response.xpath('//meta[@name="keywords"]/@content').get()
    #     item['nachricht_text'] = get_text(response)  # response.xpath('//article').get()
    #     item['nachricht_date'] = response.xpath('//meta[@name="date"]/@content').get()
    #     # item['nachricht_extern_links'] = "LINKS"  # response.xpath('')
    #     print(item.items())
