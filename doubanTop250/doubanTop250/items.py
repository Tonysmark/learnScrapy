# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMovietop250Item(scrapy.Item):
    # define the fields for your item here like:
    number = scrapy.Field()
    title_zh = scrapy.Field()
    rating = scrapy.Field()
    intro = scrapy.Field()
    evaluate = scrapy.Field()
    quote = scrapy.Field()
    pass


class DoubanMusictop250Item(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    releaceDate = scrapy.Field()
    musicGenre = scrapy.Field()
    rating = scrapy.Field()
    evaluate = scrapy.Field()
    pass
