# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherquanguoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ls_position_name = scrapy.Field()
    ls_weather1 = scrapy.Field()
    ls_weather2 = scrapy.Field()
    ls_weather3 = scrapy.Field()
    ls_weather4 = scrapy.Field()
    ls_weather5 = scrapy.Field()
    ls_weather6 = scrapy.Field()
    ls_weather7 = scrapy.Field()
    ls_weather8 = scrapy.Field()
