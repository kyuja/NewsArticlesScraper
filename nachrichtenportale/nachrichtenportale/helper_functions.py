from .portal import Portal
import csv
from urllib.parse import urlparse


def get_domain(response):
    parsed_uri = urlparse(response.url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain


def get_text(response):
    text = response.xpath('//article//text()').getall()
    text = ' '.join(text).strip()
    return text


def read_csv_to_list(csv_file):
    portale = []
    # '../nachrichtenportale/nachrichtenportale/data/Portale.csv'
    with open(csv_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            portal = Portal(row['start_url'], row['allowed_domains'], row['homepage'], row['article'])
            portale.append(portal)
    return portale