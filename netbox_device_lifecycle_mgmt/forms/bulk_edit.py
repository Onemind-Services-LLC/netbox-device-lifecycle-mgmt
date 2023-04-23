from dcim.models import DeviceType, InventoryItem
from netbox.forms import NetBoxModelBulkEditForm
from utilities.forms.fields import DynamicModelChoiceField

from ..models import *

__all__ = [
    'HardwareNoticeBulkEditForm',
]


class HardwareNoticeBulkEditForm(NetBoxModelBulkEditForm):
    device_type = DynamicModelChoiceField(queryset=DeviceType.objects.all(), required=False)

    inventory_item = DynamicModelChoiceField(queryset=InventoryItem.objects.all(), required=False)

    model = HardwareNotice
