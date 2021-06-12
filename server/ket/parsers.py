from rest_framework.parsers import JSONParser

from apps.contrib.utils import convert_json, camel_to_snake


class PayloadConversionParser(JSONParser):
    def parse(self, stream, media_type=None, parser_context=None):
        try:
            payload = super().parse(stream, media_type, parser_context)
            payload = convert_json(payload, camel_to_snake)
            return payload
        except Exception as e:
            raise e
