import django_tables2 as tables
from netbox.tables import NetBoxTable, columns

from .models import *

__all__ = ['HardwareNoticeTable', 'SoftwareNoticeTable', 'SoftwareImageTable']


class HardwareNoticeTable(NetBoxTable):
    object_type = columns.ContentTypeColumn(verbose_name='Object type')

    object = tables.Column(linkify=True, orderable=False, verbose_name='Object')

    comments = columns.MarkdownColumn()

    tags = columns.TagColumn(url_name='plugins:netbox_device_lifecycle_mgmt:hardwarenotice_list')

    class Meta(NetBoxTable.Meta):
        model = HardwareNotice
        fields = (
            'pk',
            'id',
            'object_type',
            'object',
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
            'object_type',
            'object',
            'description',
            'release_date',
            'end_of_sale_date',
        )


class SoftwareNoticeTable(NetBoxTable):
    platform = tables.Column(linkify=True)

    comments = columns.MarkdownColumn()

    tags = columns.TagColumn(url_name='plugins:netbox_device_lifecycle_mgmt:softwarenotice_list')

    class Meta(NetBoxTable.Meta):
        model = SoftwareNotice
        fields = (
            'pk',
            'id',
            'platform',
            'version',
            'release_date',
            'end_of_support_date',
            'documentation_url',
            'long_term_support',
            'pre_release',
            'created',
            'last_updated',
            'tags',
            'comments',
        )

        default_columns = (
            'id',
            'platform',
            'version',
            'release_date',
            'end_of_support_date',
        )


class SoftwareImageTable(NetBoxTable):
    software = tables.Column(linkify=True)

    file_name = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = SoftwareImage
        fields = (
            'pk',
            'id',
            'software',
            'file_name',
            'download_url',
            'sha256sum_checksum',
            'default_image',
            'description',
            'comments',
            'tags',
            'created',
            'last_updated',
        )

        default_columns = (
            'id',
            'name',
            'software',
            'file_name',
            'default_image',
            'description',
        )
