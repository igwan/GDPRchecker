# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from crawler.items import FormLoader, InputLoader
from helpers import default_scheme, get_domain


class FormSpider(CrawlSpider):
    """Form spider"""
    name = 'form'

    rules = [
        Rule(LinkExtractor(), callback='parse_page', follow=True)
    ]

    def __init__(self, urls, auth, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if auth:
            auth_split = auth.split(':')
            self.http_user = auth_split[0]
            self.http_pass = auth_split[1]

        urls = list(map(default_scheme, urls))
        domains = list(set(map(get_domain, urls)))

        self.start_urls = urls
        self.allowed_domains = domains

    def parse_page(self, response):
        return [self.parse_form(form, response)
                for form in response.xpath('//form')]

    def parse_form(self, selector, response):
        f = FormLoader(selector=selector)
        f.add_value('url', response.url)
        f.add_xpath('action', '@action')
        f.add_value(
            'inputs',
            [self.parse_input(input_field)
             for input_field in selector.xpath('//input')
             if self.is_input_field(input_field)]
        )
        return f.load_item()

    def is_input_field(self, input_field):
        input_type = next(iter(input_field.xpath('@type').extract()), None)
        return input_type not in ['hidden', 'submit']

    def parse_input(self, selector):
        i = InputLoader(selector=selector)
        i.add_xpath('type', '@type')
        i.add_xpath('name', '@name')
        i.add_xpath('id', '@id')
        return i.load_item()
