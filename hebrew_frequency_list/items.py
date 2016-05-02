# -*- coding: utf-8 -*-

import scrapy


class HebrewFrequencyListItem(scrapy.Item):
    rank = scrapy.Field()
    english = scrapy.Field()
    transliteration = scrapy.Field()
    hebrew = scrapy.Field()
