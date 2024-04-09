from scrapy.item import Item, Field

class ImageItem(Item):
    url = Field()
    name = Field()
    category = Field()