from dcim.models import DeviceType, InventoryItem, ModuleType, Platform
from django import forms
from netbox.forms import NetBoxModelForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from utilities.forms.widgets import DatePicker

from ..models import *

__all__ = ['HardwareNoticeForm', 'SoftwareNoticeForm', 'SoftwareImageForm']


class HardwareNoticeForm(NetBoxModelForm):
    device_type = DynamicModelChoiceField(queryset=DeviceType.objects.all(), required=False, selector=True)

    inventory_item = DynamicModelChoiceField(queryset=InventoryItem.objects.all(), required=False, selector=True)

    module_type = DynamicModelChoiceField(queryset=ModuleType.objects.all(), required=False, selector=True)

    comments = CommentField()

    fieldsets = (
        (None, ('device_type', 'inventory_item', 'module_type', 'description', 'tags')),
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
            'module_type',
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
            elif isinstance(instance.object, ModuleType):
                initial['module_type'] = instance.object

        kwargs['initial'] = initial

        super().__init__(*args, **kwargs)

    def clean(self):
        super().clean()

        # Handle object assignment
        selected_objects = [
            field for field in ('device_type', 'inventory_item', 'module_type') if self.cleaned_data[field]
        ]

        if len(selected_objects) > 1:
            raise forms.ValidationError(
                {selected_objects[1]: "A Hardware Notice can only be assigned to a single object."},
            )
        elif selected_objects:
            self.instance.object = self.cleaned_data[selected_objects[0]]
        else:
            self.instance.object = None


class SoftwareNoticeForm(NetBoxModelForm):
    platform = DynamicModelChoiceField(queryset=Platform.objects.all(), required=False, selector=True)

    comments = CommentField()

    fieldsets = (
        (None, ('platform', 'version', 'description', 'tags')),
        ('Lifecycle Management', ('release_date', 'end_of_support_date', 'long_term_support', 'pre_release')),
        ('Additional Information', ('documentation_url',)),
    )

    class Meta:
        model = SoftwareNotice
        fields = [
            'platform',
            'version',
            'release_date',
            'end_of_support_date',
            'documentation_url',
            'long_term_support',
            'pre_release',
            'comments',
            'tags',
            'description',
        ]
        widgets = {
            'release_date': DatePicker(),
            'end_of_support_date': DatePicker(),
        }


class SoftwareImageForm(NetBoxModelForm):
    software = DynamicModelChoiceField(queryset=SoftwareNotice.objects.all(), selector=True)

    comments = CommentField()

    fieldsets = (
        (None, ('file_name', 'software', 'description', 'tags')),
        ('Attributes', ('download_url', 'sha256_checksum', 'default_image')),
    )

    class Meta:
        model = SoftwareImage
        fields = [
            'software',
            'file_name',
            'download_url',
            'sha256_checksum',
            'default_image',
            'description',
            'comments',
            'tags',
        ]
