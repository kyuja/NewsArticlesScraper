from scrapy import Item
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class PortalItem:
    portal: Optional[str] = field(default=None)
    today: Optional[str] = field(default=None)
    url: Optional[str] = field(default=None)
    title: Optional[str] = field(default=None)
    keywords: Optional[str] = field(default=None)
    text: Optional[str] = field(default=None)
    date: Optional[str] = field(default=None)
