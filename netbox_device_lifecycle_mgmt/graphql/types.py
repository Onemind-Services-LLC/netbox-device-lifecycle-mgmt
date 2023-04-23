from netbox.graphql.types import NetBoxObjectType

from .. import models

__all__ = [
    'HardwareNoticeType',
    'SoftwareNoticeType',
    'SoftwareImageType',
]


class HardwareNoticeType(NetBoxObjectType):
    class Meta:
        model = models.HardwareNotice
        fields = '__all__'


class SoftwareNoticeType(NetBoxObjectType):
    class Meta:
        model = models.SoftwareNotice
        fields = '__all__'


class SoftwareImageType(NetBoxObjectType):
    class Meta:
        model = models.SoftwareImage
        fields = '__all__'
