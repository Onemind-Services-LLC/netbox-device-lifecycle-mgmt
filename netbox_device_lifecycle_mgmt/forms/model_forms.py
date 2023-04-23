from dcim.models import DeviceType, InventoryItem
from django import forms
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

    def __init__(self, *args, **kwargs):
        # Initialize helper selectors
        instance = kwargs.get('instance')
        initial = kwargs.get('initial', {}).copy()
        if instance:
            if isinstance(instance.object, DeviceType):
                initial['device_type'] = instance.object
            elif isinstance(instance.object, InventoryItem):
                initial['inventory_item'] = instance.object

        kwargs['initial'] = initial

        super().__init__(*args, **kwargs)

    def clean(self):
        super().clean()

        # Handle object assignment
        selected_objects = [field for field in ('device_type', 'inventory_item') if self.cleaned_data[field]]

        if len(selected_objects) > 1:
            raise forms.ValidationError(
                {selected_objects[1]: "A Hardware Notice can only be assigned to a single object."},
            )
        elif selected_objects:
            self.instance.object = self.cleaned_data[selected_objects[0]]
        else:
            self.instance.object = None
