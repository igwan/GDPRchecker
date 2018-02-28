GDPRchecker
===========

Overview
--------

Try to give hints about some steps required to make a website GDPR_ compliant. Use scrapy_ to crawl one or many urls, without crossing the domain boundary, looking for form fields and extract their inputs name.

Requirements
------------

* Python 3
* pipenv_

Installation
------------

    $ pipenv install

Then either enter a pipenv shell using:

    $ pipenv shell

Or prefix ``gdprchecker`` commands with ``pipenv run`` like so:

    $ pipenv run ./gdprchecker www.example.com

Usage
-----

::

    $ gdprchecker
    usage: gdprchecker [-h] [-f] [-s] [--auth AUTH] [--no-crawl] [--no-robotstxt]
                       [-v]
                       url [url ...]

    Try to give hints about some steps required to make a website GDPR compliant.
    If no check flag is passed do all checks.

    positional arguments:
      url             One or many urls to check

    optional arguments:
      -h, --help      show this help message and exit
      -f, --form      Check for forms
      -s, --https     Check for https
      --auth AUTH     Credentials for basic auth (user:passwd)
      --no-crawl      Do not crawl the whole website, only check the given urls
      --no-robotstxt  When crawling do not obey robots.txt
      -v, --verbose   Print more information about what is happening. This option
                      is repeatable and will increase verbosity each time it is
                      repeated.


.. _GDPR: https://en.wikipedia.org/wiki/General_Data_Protection_Regulation
.. _scrapy: https://docs.scrapy.org/
.. _pipenv: https://docs.pipenv.org/
