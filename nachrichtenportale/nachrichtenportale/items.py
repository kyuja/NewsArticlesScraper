# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from dataclasses import dataclass


@dataclass
class PortalItem(Item):
    portal = Field()
    today = Field()
    nachricht_url = Field()
    nachricht_title = Field(default='Nicht angegeben')
    nachricht_keywords = Field(default='Nicht angegeben')
    nachricht_text = Field()
    nachricht_date = Field(default='Nicht angegeben')
    # nachricht_extern_links = Field()
