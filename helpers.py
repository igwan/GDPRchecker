from urllib.parse import urlparse


def get_domain(url):
    return urlparse(url).netloc.split('@')[0].split(':')[-1]


def default_scheme(url):
    parsed_url = urlparse(url)
    return url if parsed_url.scheme else 'http://' + url
