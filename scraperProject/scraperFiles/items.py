from dataclasses import dataclass, field
from typing import Optional


@dataclass
class PortalItem:
    portal: str | None = field(default=None)
    today: str | None = field(default=None)
    url: str | None = field(default=None)
    title: str | None = field(default=None)
    keywords: str | None = field(default=None)
    text: str | None = field(default=None)
    date: str | None = field(default=None)
