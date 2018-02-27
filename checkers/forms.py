"""Crawl a some urls looking for form and return their url and fields"""

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from clint.textui import indent, colored, puts


def check(urls, auth=None, crawl=True, robotstxt=True, verbosity=0):
    """Crawl a list of url"""
    # we somehow need to append an empty string for bold to work
    puts(colored.white('Checking forms:', bold=True) + '')
    settings = get_project_settings()

    if verbosity > 0:
        settings.set('LOG_ENABLED', True)
        log_levels = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG']
        if verbosity >= len(log_levels):
            verbosity = len(log_levels) - 1
        settings.set('LOG_LEVEL', log_levels[verbosity])

    if not robotstxt:
        settings.set('ROBOTSTXT_OBEY', False)

    process = CrawlerProcess(settings)
    crawler = process.create_crawler('form')

    crawler.signals.connect(_crawler_result, scrapy.signals.item_scraped)

    process.crawl(crawler, urls=urls, crawl=crawl, auth=auth)
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
