import scrapy


class ZeitSpider(scrapy.Spider):
    name = "Zeit"
    allowed_domains = ["zeit.de"]
    start_urls = ["https://zeit.de"]

    def parse(self, response):
        pass
