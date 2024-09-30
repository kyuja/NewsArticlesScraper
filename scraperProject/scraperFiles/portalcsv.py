class PortalCSV:
    url: str
    allowed_domain: str
    homepage: str
    article: str

    def __init__(self, url, domain, homepage, article, crawler):
        self.url = url
        self.allowed_domain = domain
        self.homepage = homepage
        self.article = article
        self.crawler = crawler

    def __str__(self):
        return self.allowed_domain

    def get_url(self) -> str:
        return self.url

    def get_allowed_domain(self) -> str:
        return self.allowed_domain

    def get_homepage(self) -> str:
        return self.homepage

    def get_article(self) -> str:
        return self.article

    def get_crawler(self) -> str:
        return self.crawler
