import logging

from rest_framework import viewsets
from rest_framework.response import Response

logger = logging.getLogger(__name__)


class AuthViewSet(viewsets.ViewSet):
    def create(self, request, format=None):
        try:
            logger.info(request.data)
        except Exception as e:
            raise e
        else:
            return Response(True)
