from netbox.forms import NetBoxModelImportForm

from ..models import *

__all__ = [
    'HardwareNoticeImportForm',
    'SoftwareNoticeImportForm',
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
        )
