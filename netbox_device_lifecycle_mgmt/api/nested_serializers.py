from netbox.api.serializers import WritableNestedSerializer
from rest_framework import serializers

from ..models import *

__all__ = [
    'NestedHardwareNoticeSerializer',
    'NestedSoftwareNoticeSerializer',
    'NestedSoftwareImageSerializer',
    'NestedSoftwareImageAssociationSerializer',
]


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


class NestedSoftwareImageAssociationSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_device_lifecycle_mgmt-api:softwareimageassociation-detail',
    )

    class Meta:
        model = SoftwareImageAssociation
        fields = (
            'id',
            'url',
            'display',
        )
