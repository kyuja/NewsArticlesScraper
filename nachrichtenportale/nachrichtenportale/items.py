# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class NachrichtenportalItem(Item):
    portal = Field()
    today = Field()
    nachricht_url = Field()
    nachricht_title = Field()
    nachricht_keywords = Field()
    nachricht_text = Field()
    nachricht_date = Field()
    nachricht_extern_links = Field()

