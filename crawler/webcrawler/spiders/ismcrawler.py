# Scrapy
import scrapy

# Misc
import string
import re

# Items
from webcrawler.items import HumanName

# Base alphabet
english_alphabet = string.ascii_lowercase

# Custom alphabet
uzbek_alphabet = re.sub('w', '', english_alphabet)
uzbek_alphabet = re.sub('c', '', english_alphabet)
uzbek_alphabet = [
    letter for letter in uzbek_alphabet] + ['o‘', 'g‘', 'sh', 'ch']


class IsmcrawlerSpider(scrapy.Spider):
    name = 'ismcrawler'
    allowed_domains = ['ism.uz']
    start_urls = ['http://ism.uz/']

    def start_requests(self):
        boys_name_base_url = 'http://ism.uz/letter/boy/{letter}'
        girls_name_base_url = 'http://ism.uz/letter/girl/{letter}'
        boys_name_urls = [
            boys_name_base_url.format(letter=letter)
            for letter in uzbek_alphabet]
        girls_name_urls = [
            girls_name_base_url.format(letter=letter)
            for letter in uzbek_alphabet]
        all_urls = boys_name_urls + girls_name_urls
        return [scrapy.Request(url=url) for url in all_urls]

    def parse(self, response):
        def sanitize(items): return [
            i.replace(
                '\n',
                '').replace(
                '\t',
                '').strip().split()[0].lower() for i in items]
        ismlar_raw = scrapy.selector.Selector(response).xpath(
            '/html/body/div[2]/div[1]/div/div/ul/li/a/text()').extract()
        ismlar_raw = scrapy.selector.Selector(response).xpath(
            '/html/body/div[2]/div[1]/div/div/ul/li/a/text()').extract()
        ismlar = sanitize(ismlar_raw)

        for ism in ismlar:
            def gender(url): return 'male' if 'boy' in url else 'female'
            item = HumanName()
            item['name'] = ism
            item['gender'] = gender(response.url)
            yield item
