import logging

from djangorestframework_camel_case.render import CamelCaseJSONRenderer, CamelCaseBrowsableAPIRenderer

logger = logging.getLogger(__name__)


class PayloadConversionJSONRenderer(CamelCaseJSONRenderer):
    def render(self, data, *args, **kwargs):
        payload = super().render(data, *args, **kwargs)
        logger.info(payload)
        return payload


class PayloadConversionBrowsableAPIRenderer(CamelCaseBrowsableAPIRenderer):
    def render(self, data, *args, **kwargs):
        payload = super().render(data, *args, **kwargs)
        logger.info(payload)
        return payload
