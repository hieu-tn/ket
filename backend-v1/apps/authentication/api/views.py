import logging

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..utils import ChallengeSwitcher

logger = logging.getLogger(__name__)


class AuthViewSet(viewsets.ViewSet):
    def create(self, request, format=None):
        try:
            logger.info(request.data)
        except Exception as e:
            raise e
        else:
            # return Response(True)
            return Response({
                'is_success': True
            })

    @action(methods=['post'], detail=False, url_path='challenge', url_name='Respond to challenge')
    def respond_to_challenge(self, request, format=None):
        try:
            return ChallengeSwitcher.process_challenge(request=request)
        except Exception as e:
            raise e
