import json
import logging

from django.template.response import TemplateResponse
from django.utils.deprecation import MiddlewareMixin

from apps.contrib.utils import camel_to_snake, convert_json, snake_to_camel

logger = logging.getLogger(__name__)


class PayloadConversionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            request_data = getattr(request, '_body', request.body)
            if request_data and request.content_type == 'application/json':
                logger.info(request_data)
                request_data = json.loads(request_data.decode('utf-8'))
                request_data = convert_json(request_data, camel_to_snake)
                request_data = json.dumps(request_data).encode('utf-8')
                setattr(request, '_body', request_data)
        except Exception as e:
            raise e

    def process_response(self, request, response):
        try:
            response_data = getattr(response, 'data', response.content)
            if response_data and isinstance(response_data, dict) and not isinstance(response, TemplateResponse):
                logger.info(response.data)
                response_data = convert_json(response_data, snake_to_camel)
                response_data = json.dumps(response_data).encode('utf-8')
                setattr(response, 'content', response_data)
                response.render()
        except Exception as e:
            raise e
        else:
            return response
