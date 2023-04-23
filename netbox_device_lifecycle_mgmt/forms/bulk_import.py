from netbox.forms import NetBoxModelImportForm

from ..models import *

__all__ = [
    'HardwareNoticeImportForm',
    'SoftwareNoticeImportForm',
    'SoftwareImageImportForm',
    'SoftwareImageAssociationImportForm',
    'ServiceProviderImportForm',
    'ContractImportForm',
]


class HardwareNoticeImportForm(NetBoxModelImportForm):
    class Meta:
        model = HardwareNotice
        fields = (
            # TODO: Add object selector
            'release_date',
            'end_of_sale_date',
            'end_of_support_date',
            'end_of_sw_releases_date',
            'end_of_security_updates_date',
            'description',
            'tags',
            'comments',
            'description',
            'documentation_url',
        )


class SoftwareNoticeImportForm(NetBoxModelImportForm):
    class Meta:
        model = SoftwareNotice
        fields = (
            'platform',
            'version',
            'release_date',
            'end_of_support_date',
            'documentation_url',
            'long_term_support',
            'pre_release',
            'description',
            'tags',
            'comments',
        )


class SoftwareImageImportForm(NetBoxModelImportForm):
    class Meta:
        model = SoftwareImage
        fields = (
            'software',
            'file_name',
            'download_url',
            'sha256_checksum',
            'default_image',
            'description',
            'tags',
            'comments',
        )


class SoftwareImageAssociationImportForm(NetBoxModelImportForm):
    class Meta:
        model = SoftwareImageAssociation
        fields = (
            'image',
            'device_types',
            'device_roles',
            'devices',
            'inventory_items',
            'virtual_machines',
            'description',
            'tags',
            'comments',
            'valid_from',
            'valid_until',
        )


class ServiceProviderImportForm(NetBoxModelImportForm):
    class Meta:
        model = ServiceProvider
        fields = (
            'name',
            'description',
            'tags',
            'comments',
        )


class ContractImportForm(NetBoxModelImportForm):
    class Meta:
        model = Contract
        fields = (
            'service_provider',
            'name',
            'description',
            'tags',
            'comments',
        )
