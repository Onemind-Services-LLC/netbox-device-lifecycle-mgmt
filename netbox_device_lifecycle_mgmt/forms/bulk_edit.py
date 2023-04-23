from netbox.forms import NetBoxModelBulkEditForm

from ..models import *

__all__ = [
    'HardwareNoticeBulkEditForm',
    'SoftwareNoticeBulkEditForm',
]


class HardwareNoticeBulkEditForm(NetBoxModelBulkEditForm):
    model = HardwareNotice


class SoftwareNoticeBulkEditForm(NetBoxModelBulkEditForm):
    model = SoftwareNotice
