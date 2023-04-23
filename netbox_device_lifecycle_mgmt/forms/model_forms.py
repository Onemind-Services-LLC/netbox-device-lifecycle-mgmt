from dcim.models import DeviceType, InventoryItem
from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from utilities.forms.widgets import DatePicker

from ..models import *


class HardwareNoticeForm(NetBoxModelForm):
    device_type = DynamicModelChoiceField(queryset=DeviceType.objects.all(), required=False, selector=True)

    inventory_item = DynamicModelChoiceField(queryset=InventoryItem.objects.all(), required=False, selector=True)

    comments = CommentField()

    fieldsets = (
        (None, ('device_type', 'inventory_item', 'description', 'tags')),
        (
            'Lifecycle Management',
            (
                'release_date',
                'end_of_sale_date',
                'end_of_support_date',
                'end_of_sw_releases_date',
                'end_of_security_updates_date',
            ),
        ),
        ('Additional Information', ('documentation_url',)),
    )

    class Meta:
        model = HardwareNotice
        fields = [
            'device_type',
            'inventory_item',
            'release_date',
            'end_of_sale_date',
            'end_of_support_date',
            'end_of_sw_releases_date',
            'end_of_security_updates_date',
            'documentation_url',
            'comments',
            'tags',
            'description',
        ]
        widgets = {
            'release_date': DatePicker(),
            'end_of_sale_date': DatePicker(),
            'end_of_support_date': DatePicker(),
            'end_of_sw_releases_date': DatePicker(),
            'end_of_security_updates_date': DatePicker(),
        }
