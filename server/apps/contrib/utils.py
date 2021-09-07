import logging
import re

logger = logging.getLogger(__name__)


def camel_to_snake(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


def snake_to_camel(name):
    components = name.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + ''.join(x.title() for x in components[1:])


def snake_to_pascal(name):
    components = name.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return ''.join(x.title() for x in components[0:])


def convert_json(d, convert):
    new_d = {}
    for k, v in d.items():
        new_d[convert(k)] = convert_json(v, convert) if isinstance(v, dict) else v
    return new_d


def map_validation_errors_to_list(error_dict: dict):
    return [{'code': e.code, 'detail': e.message} for e in error_dict.error_list]
