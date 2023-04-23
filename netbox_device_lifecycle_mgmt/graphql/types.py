from netbox.graphql.types import NetBoxObjectType

from .. import models

__all__ = [
    'HardwareNoticeType',
]


class HardwareNoticeType(NetBoxObjectType):
    class Meta:
        model = models.HardwareNotice
        fields = '__all__'
