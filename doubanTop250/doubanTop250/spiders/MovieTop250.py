# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from doubanTop250.items import DoubanMovietop250Item


class Top250Spider(scrapy.Spider):
    name = 'MovieTop250'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response):
        # 主要解析函数
        selector = Selector(response)
        doubanItem = DoubanMovietop250Item()
        gird_view = selector.xpath("//*[@id='content']/div/div[1]/ol/li//div[@class='item']")
        # 补充 item 类型
        item: Selector
        for item in gird_view:
            # 别忘了加上相对位置 .//
            doubanItem['number'] = item.xpath(".//em/text()").extract_first()
            doubanItem['title_zh'] = item.xpath(".//span[@class='title'][position()=1]/text()").extract_first()
            # doubanItem['title_eng'] = item.xpath(".//span[@class='title'][position()=2]/text()").extract_first()
            infos = item.xpath(".//div[@class='bd']/p[1]/text()").extract()
            for info in infos:
                doubanItem['intro'] = "".join(info.split())
            doubanItem['rating'] = item.xpath(".//span[@class='rating_num']/text()").extract_first()
            doubanItem['evaluate'] = item.xpath(".//div[@class='star']/span[position()=4]/text()").extract_first()
            doubanItem['quote'] = item.xpath(".//p[@class='quote']/span/text()").extract_first()
            yield doubanItem
        nextLink = selector.xpath("//*[@id='content']//span[@class='next']/link/@href").extract()
        if nextLink:
            nextLink = nextLink[0]
            # callback 只穿函数体
            yield scrapy.Request(self.start_urls[0] + nextLink, callback=self.parse)
    pass
