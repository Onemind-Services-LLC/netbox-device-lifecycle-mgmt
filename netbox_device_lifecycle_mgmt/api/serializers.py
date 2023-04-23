from dcim.api.serializers import (
    NestedDeviceTypeSerializer,
    NestedInventoryItemSerializer,
)
from netbox.api.serializers import NetBoxModelSerializer
from rest_framework import serializers

from ..models import *

__all__ = ['HardwareNoticeSerializer']


class HardwareNoticeSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_device_lifecycle_mgmt-api:hardwarenotice-detail',
    )

    device_type = NestedDeviceTypeSerializer(
        required=False,
    )

    inventory_item = NestedInventoryItemSerializer(
        required=False,
    )

    class Meta:
        model = HardwareNotice
        fields = (
            'id',
            'url',
            'display',
            'device_type',
            'inventory_item',
            'release_date',
            'end_of_sale_date',
            'end_of_support_date',
            'end_of_sw_releases_date',
            'end_of_security_updates_date',
            'documentation_url',
            'comments',
            'tags',
            'created',
            'last_updated',
        )
