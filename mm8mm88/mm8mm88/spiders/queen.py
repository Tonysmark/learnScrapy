# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector


class QueenSpider(scrapy.Spider):
    # queen 是单页的
    name = 'queen'
    allowed_domains = ['mm8mm88.com']
    start_urls = ['http://www.mm8mm88.com/queen/']

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

    def inner(self):
        # 使用正则表达式将 pic_360 从原来的 url 中去掉
        # http://up.mm8mm88.com/pic_360/47/74/ed/4774ed62415059d554783869ee8b3b22.jpg
        # http://up.mm8mm88.com/pic/47/74/ed/4774ed62415059d554783869ee8b3b22.jpg
        patter = "pic_360"
