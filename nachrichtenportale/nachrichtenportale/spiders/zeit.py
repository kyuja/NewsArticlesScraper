import scrapy


class ZeitSpider(scrapy.Spider):
    name = "zeit"
    allowed_domains = ["zeit.de"]
    start_urls = ["https://zeit.de/index"]

    def parse(self, response):
        self.logger.info("Parse function called on %s", response.url)
        for link in response.xpath('//a/@href').getall():
            yield {
                "url": link
            }
