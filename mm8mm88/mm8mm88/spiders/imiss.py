# -*- coding: utf-8 -*-
import scrapy


class ImissSpider(scrapy.Spider):
    name = 'imiss'
    allowed_domains = ['mm8mm88.com/imiss']
    start_urls = ['http://mm8mm88.com/imiss/']

    def parse(self, response):
        pass
