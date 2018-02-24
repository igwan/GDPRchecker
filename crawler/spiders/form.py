# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from crawler.items import FormLoader, InputLoader


class FormSpider(CrawlSpider):
    name = 'form'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    rules = [
        Rule(LinkExtractor(), callback='parse_page', follow=True)
    ]

    def parse_page(self, response):
        return [self.parse_form(form, response)
                for form in response.xpath('//form')]

    def parse_form(self, selector, response):
        f = FormLoader(selector=selector)
        f.add_value('url', response.url)
        f.add_xpath('action', '@action')
        f.add_value(
            'inputs',
            [self.parse_input(input)
             for input in selector.xpath('//input')
             if self.is_input_field(input)]
        )
        return f.load_item()

    def is_input_field(self, input):
        input_type = next(iter(input.xpath('@type').extract()), None)
        return input_type not in ['hidden', 'submit']

    def parse_input(self, selector):
        i = InputLoader(selector=selector)
        i.add_xpath('type', '@type')
        i.add_xpath('name', '@name')
        i.add_xpath('id', '@id')
        return i.load_item()
