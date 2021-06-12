import logging

from rest_framework import serializers

from .models import User, Status
from ..contrib.serializers import PartialModelSerializer

logger = logging.getLogger(__name__)


class UserSerializer(PartialModelSerializer):
    def confirm(self):
        try:
            if self.instance.status not in [Status.UNCONFIRMED, Status.ARCHIVED]:
                raise serializers.ValidationError(
                    'user status is not {0} or {1}'.format(Status.UNCONFIRMED.value, Status.ARCHIVED.value)
                )

            self.initial_data = {**self.initial_data, 'status': Status.CONFIRMED}

            if self.is_valid(raise_exception=True):
                self.save()
        except Exception as e:
            raise e

    def force_change_password(self):
        try:
            self.initial_data = {**self.initial_data, 'status': Status.FORCE_CHANGE_PASSWORD}

            if self.is_valid(raise_exception=True):
                self.save()
        except Exception as e:
            raise e

    class Meta:
        model = User
        fields = '__all__'
