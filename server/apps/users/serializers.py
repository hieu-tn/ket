import logging

from rest_framework import serializers

from .models import User, Status
from ..contrib.serializers import PartialModelSerializer

logger = logging.getLogger(__name__)


class UserSerializer(PartialModelSerializer):
    user_groups = serializers.SerializerMethodField()

    def get_user_groups(self, obj):
        return [g.name for g in obj.groups.all()]

    def confirm(self):
        try:
            if self.instance.status not in [Status.FORCE_CHANGE_PASSWORD, Status.UNCONFIRMED]:
                raise serializers.ValidationError(
                    'user status is not {}'.format([Status.FORCE_CHANGE_PASSWORD.value, Status.UNCONFIRMED.value])
                )

            initial_data = getattr(self, 'initial_data', {})
            self.initial_data = {**initial_data, 'status': Status.CONFIRMED}

            if self.is_valid(raise_exception=True):
                self.save()
        except Exception as e:
            raise e

    def force_change_password(self):
        try:
            if self.instance.status in [Status.ARCHIVED]:
                raise serializers.ValidationError('user is disabled. Contact admin to activate')

            initial_data = getattr(self, 'initial_data', {})
            self.initial_data = {**initial_data, 'status': Status.FORCE_CHANGE_PASSWORD}

            if self.is_valid(raise_exception=True):
                self.save()
        except Exception as e:
            raise e

    class Meta(PartialModelSerializer.Meta):
        model = User
        fields = '__all__'
