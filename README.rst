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
    usage: gdprchecker [-h] [-v] url [url ...]
    
    Try to give hints about some steps required to make a website GDPR compliant
    
    positional arguments:
      url            One or many urls to check
    
    optional arguments:
      -h, --help     show this help message and exit
      -v, --verbose  Increase the verbosity level


.. _GDPR: https://en.wikipedia.org/wiki/General_Data_Protection_Regulation
.. _scrapy: https://docs.scrapy.org/
.. _pipenv: https://docs.pipenv.org/
