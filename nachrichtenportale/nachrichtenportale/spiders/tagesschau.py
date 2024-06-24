import scrapy


class TagesschauSpider(scrapy.Spider):
    name = "tagesschau"
    allowed_domains = ["tagesschau.de"]
    start_urls = ["https://tagesschau.de"]

    def parse(self, response):
        self.logger.info("Parse function called on %s", response.url)
        for link in response.xpath('//a[@class="teaser__link"]/@href').getall():
            yield {
                "url": link
            }

            yield scrapy.Request(response.urljoin(link), callback=self.parse)
