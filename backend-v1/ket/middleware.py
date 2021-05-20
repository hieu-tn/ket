import logging

from django.template.response import SimpleTemplateResponse
from django.utils.deprecation import MiddlewareMixin

from apps.contrib.utils import camel_to_snake, convert_json, snake_to_camel

logger = logging.getLogger(__name__)


class PayloadConversionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            if hasattr(request, 'data'):
                request.data = convert_json(request.data, camel_to_snake)
        except Exception as e:
            raise e

    def process_response(self, request, response):
        try:
            if hasattr(response, 'data') and response.data and not isinstance(response, SimpleTemplateResponse):
                response.data = convert_json(response.data, snake_to_camel)
                response._is_rendered = False
                response.render()
        except Exception as e:
            raise e
        else:
            return response
