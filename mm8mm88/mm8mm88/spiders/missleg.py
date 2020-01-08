# -*- coding: utf-8 -*-
import scrapy


class MisslegSpider(scrapy.Spider):
    name = 'missleg'
    allowed_domains = ['mm8mm88.com/missleg']
    start_urls = ['http://mm8mm88.com/missleg/']

    def parse(self, response):
        pass
