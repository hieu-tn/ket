import logging

from djangorestframework_camel_case.parser import CamelCaseFormParser, CamelCaseMultiPartParser, CamelCaseJSONParser

logger = logging.getLogger(__name__)


class NoUnderscoreBeforeNumberCamelCaseParser:
    json_underscoreize = {'no_underscore_before_number': True}


class PayloadConversionFormParser(CamelCaseFormParser, NoUnderscoreBeforeNumberCamelCaseParser):
    def parse(self, stream, media_type=None, parser_context=None):
        payload = super().parse(stream, media_type, parser_context)
        logger.info(payload)
        return payload


class PayloadConversionMultiPartParser(CamelCaseMultiPartParser, NoUnderscoreBeforeNumberCamelCaseParser):
    def parse(self, stream, media_type=None, parser_context=None):
        payload = super().parse(stream, media_type, parser_context)
        logger.info(payload)
        return payload


class PayloadConversionJSONParser(CamelCaseJSONParser, NoUnderscoreBeforeNumberCamelCaseParser):
    def parse(self, stream, media_type=None, parser_context=None):
        payload = super().parse(stream, media_type, parser_context)
        logger.info(payload)
        return payload
