# -*- coding: utf-8 -*-
import scrapy


class StunnerSpider(scrapy.Spider):
    name = 'stunner'
    allowed_domains = ['mm8mm88.com/stunner']
    start_urls = ['http://mm8mm88.com/stunner/']

    def parse(self, response):
        pass
