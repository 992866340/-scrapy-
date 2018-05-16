# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YinyueItem(scrapy.Item):
    music_id = scrapy.Field()
    music_name = scrapy.Field()
    music_img = scrapy.Field()
    music_url = scrapy.Field()
    music_singer = scrapy.Field()