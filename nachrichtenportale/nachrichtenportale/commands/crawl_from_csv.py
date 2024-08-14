# import sys # noqa
# sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))) # noqa
from ..helper_functions import read_csv_to_list
from scrapy.commands import ScrapyCommand
from scrapy.crawler import CrawlerProcess
from scrapy.exceptions import UsageError
from scrapy.utils.project import get_project_settings


class Command(ScrapyCommand):
    requires_project = True

    def syntax(self):
        return '<csv_file>'

    def short_desc(self):
        return 'Run spiders with URLs from csv file'

    def add_options(self, parser):
        ScrapyCommand.add_options(self, parser)

    def run(self, args, opts):
        if len(args) != 1:
            raise UsageError("File path needed")

        csv_file = args[0]
        process = CrawlerProcess(get_project_settings())

        portale = read_csv_to_list(csv_file)
        for portal in portale:
            process.crawl('gonnaCrawlThemAll', portal=portal)

        process.start()
