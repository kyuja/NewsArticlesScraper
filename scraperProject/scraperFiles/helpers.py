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


def check_url_ending(url):
    if url.endswith('.jsn'):
        return False
    elif url.endswith('.pdf'):
        return False
    elif url.endswith('.xml'):
        return False
    else:
        return True


def check_for_mail(url):
    if 'mailto' in url:
        return False
    else:
        return True


def check_for_javascript(url):
    if 'javascript' in url:
        return False
    else:
        return True


def check_url(url):
    if check_for_mail(url) and check_for_javascript(url):
        if 'golem' in url:
            if 'specials' in url:
                return False
        parsed_url = urlparse(url)
        if check_for_keywords(parsed_url.path) and check_url_ending(parsed_url.path):
            return True
        else:
            return False
    return False


def get_domain(url):
    url = tldextract.extract(url)
    if 'www' in url.subdomain or url.subdomain == '':
        return url.domain
    else:
        return url.subdomain
