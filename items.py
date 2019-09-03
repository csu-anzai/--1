# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #要爬取网站的对象
    title = scrapy.Field()
    link = scrapy.Field()
    comment = scrapy.Field()
