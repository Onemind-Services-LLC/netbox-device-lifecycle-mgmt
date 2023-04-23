from netbox.forms import NetBoxModelBulkEditForm

from ..models import *

__all__ = [
    'HardwareNoticeBulkEditForm',
]


class HardwareNoticeBulkEditForm(NetBoxModelBulkEditForm):
    model = HardwareNotice
