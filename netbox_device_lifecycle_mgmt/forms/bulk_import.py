from netbox.forms import NetBoxModelImportForm

from ..models import *

__all__ = [
    'HardwareNoticeImportForm',
    'SoftwareNoticeImportForm',
    'SoftwareImageImportForm',
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