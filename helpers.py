"""gdprchecker helper functions"""
from urllib.parse import urlparse
from tabulate import tabulate


def get_domain(url):
    """Return the domain of an url"""
    return urlparse(url).netloc.split('@')[0].split(':')[-1]


def default_scheme(url):
    """Add a default url scheme if missing"""
    parsed_url = urlparse(url)
    return url if parsed_url.scheme else 'http://' + url


def dict_list_to_list_dict(dict_list):
    """Transform a list of dictionaries to a dictionary of list"""
    list_dict = {}
    key_list = set(key for d in dict_list for key in d)
    for dictionary in dict_list:
        for key in key_list:
            val = dictionary.get(key)
            if key in list_dict:
                list_dict[key].append(val)
            else:
                list_dict[key] = [val]

    return list_dict


def pprint_inputs(inputs):
    """Pretty print a list of input items"""
    print(tabulate(dict_list_to_list_dict(inputs), headers='keys'))
