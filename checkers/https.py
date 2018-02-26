"""Check HTTPS connection"""

from urllib.parse import urlparse
import requests
from clint.textui import indent, colored, puts
from helpers import get_domain


def check(urls):
    """Check the urls for access through https"""
    for url in set(map(get_domain, urls)):
        puts(colored.white('Checking https for: ', bold=True)
             + colored.yellow(url))
        with indent(2):
            if check_connection(url):
                check_redirect(url)


def check_connection(url):
    """Check connection to the url using an head request over https"""
    puts('Connection ', newline=False)
    try:
        requests.head('https://' + url)
    except requests.exceptions.RequestException as err:
        print(colored.red('failed'))
        print(str(err))
        return False
    else:
        print(colored.green('success'))
        return True


def check_redirect(url):
    """Check if the url is redirecting http to https"""
    puts('Redirect ', newline=False)
    r = requests.head('http://' + url)
    if (r.status_code in [301, 302] and
            _check_redirect_location(url, r.headers['location'])):
        if r.status_code == 301:
            print(colored.green('yes'))
        else:
            print(colored.yellow(
                'yes but using a 302 redirect, consider using 301'))
    else:
        print(colored.red('no'))


def _check_redirect_location(url, location):
    parsed_location = urlparse(location)
    return (parsed_location.scheme == 'https' and
            parsed_location.netloc == url)
