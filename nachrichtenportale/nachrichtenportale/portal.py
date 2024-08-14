class Portal:
    url: str
    domain: str
    homepage: str
    article: str

    def __init__(self, url, domain, homepage, article):
        self.url = url
        self.domain = domain
        self.homepage = homepage
        self.article = article

    def __str__(self):
        return self.domain

    def get_url(self) -> str:
        return self.url

    def get_domain(self) -> str:
        return self.domain

    def get_homepage(self) -> str:
        return self.homepage

    def get_article(self) -> str:
        return self.article
