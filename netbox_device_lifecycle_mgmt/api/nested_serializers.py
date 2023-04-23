from rest_framework import serializers

from netbox.api.serializers import WritableNestedSerializer
from ..models import *

__all__ = ['NestedHardwareNoticeSerializer', 'NestedSoftwareNoticeSerializer']


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


class NestedSoftwareNoticeSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_device_lifecycle_mgmt-api:softwarenotice-detail',
    )

    class Meta:
        model = SoftwareNotice
        fields = (
            'id',
            'url',
            'display',
        )


class NestedSoftwareImageSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_device_lifecycle_mgmt-api:softwareimage-detail',
    )

    class Meta:
        model = SoftwareImage
        fields = (
            'id',
            'url',
            'display',
        )
