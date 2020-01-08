# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from doubanTop250.items import DoubanMusictop250Item


class Musictop250Spider(scrapy.Spider):
    name = 'MusicTop250'
    allowed_domains = ['music.douban.com']
    start_urls = ['http://music.douban.com/top250/']

    def parse(self, response):
        selector = Selector(response)
        item = DoubanMusictop250Item()
        table = selector.xpath("//*[@id='content']//div[@class='article']/div[@class='indent']//table")
        content: Selector
        for content in table:
            item['title'] = content.xpath('normalize-space(.//tr/td[2]//a/text())').extract_first()
            infos = content.xpath(".//tr/td[2]//p/text()").extract_first()
            item['author'] = infos.split("/")[0].strip(" ")
            item['releaceDate'] = infos.split("/")[1].strip(" ")
            item['musicGenre'] = infos.split("/")[-1].strip(" ")
            item['rating'] = content.xpath(".//tr/td[2]//span[@class='rating_nums']/text()").extract_first()
            people = content.xpath("normalize-space(.//tr/td[2]//span[3]/text())").extract_first()
            item['evaluate'] = people[2:-2]
            yield item
        nextPage = selector.xpath("//*[@id='content']//span[@class='next']/link/@href").extract()
        if nextPage:
            nextPage = nextPage[0]
        yield scrapy.Request(nextPage, callback=self.parse)
