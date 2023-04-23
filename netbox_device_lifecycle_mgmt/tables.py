import django_tables2 as tables
from netbox.tables import NetBoxTable, columns

from .models import *

__all__ = ['HardwareNoticeTable']


class HardwareNoticeTable(NetBoxTable):
    device_type = tables.Column(linkify=True)

    inventory_item = tables.Column(linkify=True)

    tags = columns.TagColumn(url_name='plugins:netbox_device_lifecycle_mgmt:hardwarenotice_list')

    class Meta(NetBoxTable.Meta):
        model = HardwareNotice
        fields = (
            'pk',
            'id',
            'device_type',
            'inventory_item',
            'description',
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
        default_columns = (
            'id',
            'device_type',
            'inventory_item',
            'description',
            'release_date',
            'end_of_sale_date',
        )
