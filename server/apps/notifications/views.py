from rest_framework import viewsets
from rest_framework.response import Response


class NotificationsViewSet(viewsets.GenericViewSet):
    authentication_classes = ()
    permission_classes = ()

    def list(self, request):
        return Response()
