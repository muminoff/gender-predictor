# -*- coding: utf-8 -*-
import scrapy


class IsmcrawlerSpider(scrapy.Spider):
    name = "ismcrawler"
    allowed_domains = ["ism.uz"]
    start_urls = ['http://ism.uz/']

    def parse(self, response):
        pass
