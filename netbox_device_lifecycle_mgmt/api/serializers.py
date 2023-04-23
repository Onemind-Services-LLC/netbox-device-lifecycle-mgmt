from django.contrib.contenttypes.models import ContentType
from netbox.api.fields import ContentTypeField
from netbox.api.serializers import NetBoxModelSerializer
from netbox.constants import NESTED_SERIALIZER_PREFIX
from rest_framework import serializers
from utilities.api import get_serializer_for_model

from ..constants import HARDWARE_NOTICE_ASSIGNMENT_MODELS
from ..models import *

__all__ = ['HardwareNoticeSerializer']


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
            'tags',
            'created',
            'last_updated',
        )

    def get_object(self, obj):
        serializer = get_serializer_for_model(obj.object, prefix=NESTED_SERIALIZER_PREFIX)
        context = {'request': self.context['request']}
        return serializer(obj.object, context=context).data
