import csv
import os
import re

from scrapy.utils.project import get_project_settings
from dataclasses import asdict
from datetime import datetime


class CsvWriterPipeline:

    def open_spider(self, spider):
        settings = get_project_settings()
        self.dir_path = settings.get('CSV_OUTPUT_PATH')
        filepath_csv = self.dir_path + spider.output_dir + '/' + spider.output_file
        os.makedirs(os.path.dirname(filepath_csv), exist_ok=True)

        self.file_exists = os.path.exists(filepath_csv)
        self.file_csv = open(filepath_csv, 'a', newline='', encoding="utf-8")
        self.writer_csv = csv.writer(self.file_csv)

    def close_spider(self, spider):
        self.file_csv.close()

    def process_item(self, item, spider):
        item_dict = asdict(item)

        if not self.file_exists:
            self.writer_csv.writerow(item_dict.keys())

        filename_txt = item_dict['title'][0]
        filename_txt = re.sub(r'\W', '', filename_txt)
        today = datetime.now().strftime('%Y-%m-%d')
        filepath_txt = self.dir_path + spider.output_dir + '/' + today + '/' + filename_txt + '.txt'
        os.makedirs(os.path.dirname(filepath_txt), exist_ok=True)

        with open(filepath_txt, 'w', encoding="utf-8") as file_txt:
            file_txt.write(item_dict['text'][0])

        item_dict['text'] = filepath_txt

        self.writer_csv.writerow(item_dict.values())
        return item
