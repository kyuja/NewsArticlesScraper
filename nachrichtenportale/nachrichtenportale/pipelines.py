import csv
import os
from scrapy.utils.project import get_project_settings
from dataclasses import fields, asdict


class CsvWriterPipeline:

    def open_spider(self, spider):
        settings = get_project_settings()
        dir_path = settings.get('CSV_OUTPUT_PATH')
        filepath = dir_path + spider.output_dir + '/' + spider.output_file
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        self.file_exists = os.path.exists(filepath)
        self.file = open(filepath, 'a', newline='')
        self.writer = csv.writer(self.file)

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        item_dict = asdict(item)

        if not self.file_exists:
            self.writer.writerow(item_dict.keys())

        self.writer.writerow(item_dict.values())
        return item