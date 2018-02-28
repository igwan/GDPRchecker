"""Crawl a some urls looking for form and return their url and fields"""

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from clint.textui import indent, colored, puts
from helpers import pprint_inputs


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
    result = Result()

    crawler.signals.connect(result.add_item, scrapy.signals.item_scraped)

    process.crawl(crawler, urls=urls, crawl=crawl, auth=auth)
    process.start()

    result.print(verbosity)


def _cmp_forms(form_a, form_b):
    return form_a['inputs'] == form_b['inputs']


class Result:
    forms = []

    def add_item(self, item, **_):
        """Called for each crawler result"""
        self._form_found(dict(item))

    def _form_found(self, form):
        duplicate = next(filter(lambda f: _cmp_forms(f, form), self.forms), None)
        if duplicate:
            duplicate['url'] += form['url']
        else:
            self.forms.append(form)

    def print(self, verbosity):
        """Print each form found"""
        for form in self.forms:
            url_count = len(form['url'])
            url = ''
            if url_count is 1:
                url = form['url'][0]
            elif url_count > 1:
                url = '{count} different urls, this is probably a search or login form'.format(
                    count=url_count)
                if verbosity > 0:
                    url += "\n" + str(form['url'])

            puts(colored.green("Found form at ") + url)
            puts(colored.green("With the following fields:"))
            with indent(4):
                pprint_inputs(form['inputs'])
