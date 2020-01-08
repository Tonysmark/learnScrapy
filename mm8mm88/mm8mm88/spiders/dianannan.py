# -*- coding: utf-8 -*-
import scrapy


class DianannanSpider(scrapy.Spider):
    name = 'dianannan'
    allowed_domains = ['mm8mm88.com/dianannan']
    start_urls = ['http://mm8mm88.com/dianannan/']

    def parse(self, response):
        pass
