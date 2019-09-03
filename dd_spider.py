# -*- coding: utf-8 -*-
import scrapy
from dd.items import DdItem
from scrapy.http import Request

class DdSpiderSpider(scrapy.Spider):
    name = 'dd_spider'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://www.dangdang.com/']

    #回调函数
    def parse(self, response):
        item = DdItem()
        #提取标题
        item["title"] = response.xpath("//a[@class='pic']/@title").extract()
        #提取链接
        item["link"] = response.xpath("//a[@class='pic']/@href").extract()
        #提取评价
        item["comment"] = response.xpath("//a[@class='search_comment_num']/text()").extract()
        yield item
        for i in range(1, 20):
            url = "http://category.dangdang.com/pg" + str(i) + "-cp01.54.06.00.00.00.html"
            yield Request(url, callback=self.parse)
