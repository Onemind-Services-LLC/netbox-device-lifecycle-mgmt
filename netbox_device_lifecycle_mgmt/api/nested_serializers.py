from netbox.api.serializers import WritableNestedSerializer
from rest_framework import serializers

from ..models import *

__all__ = ['NestedHardwareNoticeSerializer']


class NestedHardwareNoticeSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_device_lifecycle_mgmt-api:hardwarenotice-detail',
    )

    class Meta:
        model = HardwareNotice
        fields = (
            'id',
            'url',
            'display',
        )
