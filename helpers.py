"""gdprchecker helper functions"""
from urllib.parse import urlparse


def get_domain(url):
    """Return the domain of an url"""
    return urlparse(url).netloc.split('@')[0].split(':')[-1]


def default_scheme(url):
    """Add a default url scheme if missing"""
    parsed_url = urlparse(url)
    return url if parsed_url.scheme else 'http://' + url
