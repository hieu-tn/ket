import logging
import uuid

from rest_framework.permissions import BasePermission

logger = logging.getLogger(__name__)


class UserAccessOneOwnResourcePermission(BasePermission):
    """
    Allows user accesses only one's own resource.
    """

    def has_permission(self, request, view):
        return bool(request.user.user_uuid == uuid.UUID(view.kwargs['user_uuid']))
