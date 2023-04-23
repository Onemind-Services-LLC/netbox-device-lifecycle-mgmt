import django_tables2 as tables
from netbox.tables import NetBoxTable, columns
from utilities.forms.fields import ChoiceField

from .choices import *
from .models import *

__all__ = [
    'HardwareNoticeTable',
    'SoftwareNoticeTable',
    'SoftwareImageTable',
    'SoftwareImageAssociationTable',
    'ServiceProviderTable',
    'ContractTable',
]


class HardwareNoticeTable(NetBoxTable):
    object_type = columns.ContentTypeColumn(verbose_name='Object type')

    object = tables.Column(linkify=True, orderable=False, verbose_name='Object')

    comments = columns.MarkdownColumn()

    tags = columns.TagColumn(url_name='plugins:netbox_device_lifecycle_mgmt:hardwarenotice_list')

    release_date = tables.DateColumn(
        verbose_name='Release Date',
    )

    end_of_sale_date = tables.DateColumn(
        verbose_name='End of Sale',
    )

    end_of_support_date = tables.DateColumn(
        verbose_name='End of Support',
    )

    end_of_sw_releases_date = tables.DateColumn(
        verbose_name='End of Software Releases',
    )

    end_of_security_updates_date = tables.DateColumn(
        verbose_name='End of Security Updates',
    )

    documentation_url = tables.Column(
        verbose_name='Documentation URL',
    )

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

    release_date = tables.DateColumn(
        verbose_name='Release Date',
    )

    end_of_support_date = tables.DateColumn(
        verbose_name='End of Support',
    )

    documentation_url = tables.Column(
        verbose_name='Documentation URL',
    )

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

    file_name = tables.Column(linkify=True, verbose_name='File Name')

    download_url = tables.Column(linkify=True, verbose_name='Download URL')

    sha256sum_checksum = tables.Column(verbose_name='SHA256 Checksum')

    default_image = tables.BooleanColumn(verbose_name='Default Image')

    tags = columns.TagColumn(url_name='plugins:netbox_device_lifecycle_mgmt:softwareimage_list')

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


class SoftwareImageAssociationTable(NetBoxTable):
    image = tables.Column(linkify=True)

    tags = columns.TagColumn(url_name='plugins:netbox_device_lifecycle_mgmt:softwareimageassociation_list')

    class Meta(NetBoxTable.Meta):
        model = SoftwareImageAssociation
        fields = (
            'pk',
            'id',
            'image',
            'device_types',
            'device_roles',
            'devices',
            'inventory_items',
            'virtual_machines',
            'created',
            'last_updated',
            'tags',
            'description',
            'comments',
        )

        default_columns = (
            'id',
            'image',
            'device_types',
            'device_roles',
            'devices',
            'inventory_items',
            'virtual_machines',
        )


class ServiceProviderTable(NetBoxTable):
    name = tables.Column(linkify=True)

    tags = columns.TagColumn(url_name='plugins:netbox_device_lifecycle_mgmt:serviceprovider_list')

    class Meta(NetBoxTable.Meta):
        model = ServiceProvider
        fields = (
            'pk',
            'id',
            'name',
            'description',
            'comments',
            'tags',
            'created',
            'last_updated',
        )

        default_columns = (
            'id',
            'name',
            'description',
        )


class ContractTable(NetBoxTable):
    name = tables.Column(linkify=True)

    service_provider = tables.Column(linkify=True)

    start_date = tables.DateColumn(
        verbose_name='Start Date',
    )

    end_date = tables.DateColumn(
        verbose_name='End Date',
    )

    renewal_date = tables.DateColumn(
        verbose_name='Renewal Date',
    )

    # contract_type = ChoiceField(
    #     choices=ContractTypeChoices,
    # )

    tags = columns.TagColumn(url_name='plugins:netbox_device_lifecycle_mgmt:contract_list')

    class Meta(NetBoxTable.Meta):
        model = Contract
        fields = (
            'pk',
            'id',
            'name',
            'description',
            'service_provider',
            'contract_number',
            'contract_type',
            'start_date',
            'end_date',
            'renewal_date',
            'cost',
            'currency',
            'contract_type',
            'comments',
            'tags',
            'created',
            'last_updated',
        )

        default_columns = (
            'id',
            'name',
            'service_provider',
            'contract_number',
            'contract_type',
            'start_date',
            'end_date',
        )
