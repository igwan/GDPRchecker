# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join


class Form(scrapy.Item):
    url = scrapy.Field()
    action = scrapy.Field(
        output_processor=TakeFirst()
    )
    inputs = scrapy.Field()


class FormLoader(ItemLoader):
    default_item_class = Form


class Input(scrapy.Item):
    type = scrapy.Field()
    name = scrapy.Field()
    id = scrapy.Field()


class InputLoader(ItemLoader):
    default_item_class = Input
    default_output_processor = TakeFirst()
