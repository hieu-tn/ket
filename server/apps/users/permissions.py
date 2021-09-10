import logging
import uuid

from rest_framework.permissions import BasePermission

from .models import Status

logger = logging.getLogger(__name__)


class UserAccessOneOwnRecordPermission(BasePermission):
    """
    Allows user accesses only one's own resource.
    """

    def has_permission(self, request, view):
        return bool(request.user.user_uuid == uuid.UUID(view.kwargs['user_uuid']))


class IsUserConfirmed(BasePermission):
    """
    Allows only confirmed user to perform actions
    """

    def has_permission(self, request, view):
        return bool(request.user.status == Status.CONFIRMED)
