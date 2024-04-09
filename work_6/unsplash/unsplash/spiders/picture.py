import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import csv

class ImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        return 'full/' + request.url.split('/')[-1]

    def item_completed(self, results, item, info):
        if not results:
            raise DropItem("Image Download Failed")
        item['local_path'] = [x['path'] for ok, x in results if ok]
        return item
    
class CSVExportPipeline(object):
    def __init__(self):
        self.csv_file = open('images.csv', 'w', newline='')
        self.csv_writer = csv.writer(self.csv_file)
        self.csv_writer.writerow(['URL', 'Local Path', 'Name', 'Category'])

    def close_spider(self, spider):
        self.csv_file.close()

    def process_item(self, item, spider):
        self.csv_writer.writerow([item['url'], item['local_path'], item['name'], item['category']])
        return item