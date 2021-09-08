from rest_framework import serializers
from rest_framework.fields import empty


class PartialModelSerializer(serializers.ModelSerializer):
    def __init__(self, instance=None, data=empty, **kwargs):
        super().__init__(instance=instance, data=data, **kwargs)
        self.partial = True

    class Meta:
        pass
