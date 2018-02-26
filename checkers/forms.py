"""Crawl a some urls looking for form and return their url and fields"""

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from clint.textui import indent, colored, puts


def check(urls, verbose):
    """Crawl a list of url"""
    settings = get_project_settings()
    settings.update({
        'LOG_ENABLED': verbose > 0,
        'STATS_DUMP': False
    })

    process = CrawlerProcess(settings)
    crawler = process.create_crawler('form')

    crawler.signals.connect(_crawler_result, scrapy.signals.item_scraped)

    process.crawl(crawler, urls=urls)
    process.start()


def _crawler_result(item, **_):
    """Called for each crawler result"""
    _form_found(dict(item))


def _form_found(form):
    """Print each form found"""
    puts(colored.green("Found form at ") + form['url'])
    puts(colored.green("With the following field:"))
    with indent(4):
        for input_field in form['inputs']:
            puts(input_field['name'])
