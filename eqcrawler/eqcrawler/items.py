# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field


class EarthquakeItem(Item):
    id = Field()
    date = Field()
    lattitude = Field()
    longitude = Field()
    depth = Field()
    magnitude = Field()
    region = Field()
