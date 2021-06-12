import logging

from rest_framework.renderers import JSONRenderer

from apps.contrib.utils import convert_json, snake_to_camel

logger = logging.getLogger(__name__)


class PayloadConversionRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if isinstance(data, dict):
            data = convert_json(data, snake_to_camel)

        return super().render(data, accepted_media_type, renderer_context)
