# -*- coding: utf-8 -*-
import scrapy


class BololiSpider(scrapy.Spider):
    name = 'bololi'
    allowed_domains = ['mm8mm88.com/bololi']
    start_urls = ['http://mm8mm88.com/bololi/']

    def parse(self, response):
        pass
