from dcim.api.nested_serializers import (
    NestedDeviceRoleSerializer,
    NestedDeviceSerializer,
    NestedDeviceTypeSerializer,
    NestedInventoryItemSerializer,
    NestedPlatformSerializer,
)
from dcim.models import Device, DeviceRole, DeviceType, InventoryItem
from django.contrib.contenttypes.models import ContentType
from netbox.api.fields import ContentTypeField, SerializedPKRelatedField
from netbox.api.serializers import NetBoxModelSerializer
from netbox.constants import NESTED_SERIALIZER_PREFIX
from rest_framework import serializers
from utilities.api import get_serializer_for_model
from virtualization.api.nested_serializers import NestedVirtualMachineSerializer
from virtualization.models import VirtualMachine

from ..constants import HARDWARE_NOTICE_ASSIGNMENT_MODELS
from ..models import *
from .nested_serializers import *

__all__ = [
    'HardwareNoticeSerializer',
    'SoftwareNoticeSerializer',
    'SoftwareImageSerializer',
    'SoftwareImageAssociationSerializer',
    'ServiceProviderSerializer',
]


class HardwareNoticeSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_device_lifecycle_mgmt-api:hardwarenotice-detail',
    )

    object_type = ContentTypeField(
        queryset=ContentType.objects.filter(HARDWARE_NOTICE_ASSIGNMENT_MODELS),
        required=False,
        allow_null=True,
    )
    object = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = HardwareNotice
        fields = (
            'id',
            'url',
            'display',
            'object_type',
            'object_id',
            'object',
            'release_date',
            'end_of_sale_date',
            'end_of_support_date',
            'end_of_sw_releases_date',
            'end_of_security_updates_date',
            'documentation_url',
            'comments',
            'description',
            'tags',
            'created',
            'last_updated',
        )

    def get_object(self, obj):
        serializer = get_serializer_for_model(obj.object, prefix=NESTED_SERIALIZER_PREFIX)
        context = {'request': self.context['request']}
        return serializer(obj.object, context=context).data


class SoftwareNoticeSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_device_lifecycle_mgmt-api:softwarenotice-detail',
    )

    platform = NestedPlatformSerializer()

    class Meta:
        model = SoftwareNotice
        fields = (
            'id',
            'url',
            'display',
            'platform',
            'version',
            'release_date',
            'end_of_support_date',
            'documentation_url',
            'long_term_support',
            'pre_release',
            'comments',
            'description',
            'created',
            'last_updated',
            'tags',
        )


class SoftwareImageSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_device_lifecycle_mgmt-api:softwareimage-detail',
    )

    software = NestedSoftwareNoticeSerializer()

    class Meta:
        model = SoftwareImage
        fields = (
            'id',
            'url',
            'display',
            'software',
            'file_name',
            'download_url',
            'sha256_checksum',
            'default_image',
            'comments',
            'description',
            'created',
            'last_updated',
            'tags',
        )


class SoftwareImageAssociationSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_device_lifecycle_mgmt-api:softwareimageassociation-detail',
    )

    image = NestedSoftwareImageSerializer()

    device_types = SerializedPKRelatedField(
        queryset=DeviceType.objects.all(),
        serializer=NestedDeviceTypeSerializer,
        required=False,
        many=True,
    )

    device_roles = SerializedPKRelatedField(
        queryset=DeviceRole.objects.all(),
        serializer=NestedDeviceRoleSerializer,
        required=False,
        many=True,
    )

    devices = SerializedPKRelatedField(
        queryset=Device.objects.all(),
        serializer=NestedDeviceSerializer,
        required=False,
        many=True,
    )

    inventory_items = SerializedPKRelatedField(
        queryset=InventoryItem.objects.all(),
        serializer=NestedInventoryItemSerializer,
        required=False,
        many=True,
    )

    virtual_machines = SerializedPKRelatedField(
        queryset=VirtualMachine.objects.all(),
        serializer=NestedVirtualMachineSerializer,
        required=False,
        many=True,
    )

    class Meta:
        model = SoftwareImageAssociation
        fields = (
            'id',
            'url',
            'display',
            'image',
            'device_types',
            'device_roles',
            'devices',
            'inventory_items',
            'virtual_machines',
            'comments',
            'description',
            'created',
            'last_updated',
            'tags',
        )


class ServiceProviderSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_device_lifecycle_mgmt-api:serviceprovider-detail',
    )

    class Meta:
        model = ServiceProvider
        fields = (
            'id',
            'url',
            'display',
            'name',
            'comments',
            'description',
            'created',
            'last_updated',
            'tags',
        )
