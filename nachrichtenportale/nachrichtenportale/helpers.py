from urllib.parse import urlparse
from tldextract import tldextract


def check_for_keywords(url):
    url = url.lower()
    if 'eilmeldung' in url:
        return False
    elif 'ticker' in url:
        return False
    elif 'podcast' in url:
        return False
    elif 'live' in url:
        return False
    elif 'quiz' in url:
        return False
    elif 'archiv' in url:
        return False
    else:
        return True


def check_url(url):
    parsed_url = urlparse(url)
    if check_for_keywords(parsed_url.path):
        return True
    else:
        return False


def get_domain(url):
    url = tldextract.extract(url)
    if 'www' in url.subdomain or url.subdomain == '':
        return url.domain
    else:
        return url.subdomain
