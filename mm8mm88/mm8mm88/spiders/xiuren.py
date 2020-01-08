# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

class XiurenSpider(scrapy.Spider):
    name = 'xiuren'
    allowed_domains = ['mm8mm88.com/xiuren']
    start_urls = ['http://www.mm8mm88.com/xiuren/']

    def parse(self, response):
        pageMap = {}
        selector = Selector(response)
        # 两个数组
        urls = selector.xpath(
            '//*[@id="yt_box_mm8mm88"]/div[@class="wb_listbox"]//div[@class="wb_ppic"]/dl/dt/a/@href').extract()
        names = selector.xpath(
            '//*[@id="yt_box_mm8mm88"]/div[@class="wb_listbox"]//div[@class="wb_ppic"]/dl/dt/a/text()').extract()
        for url, name in zip(urls, names):
            pageMap[name] = url
        print(pageMap)
        pass
