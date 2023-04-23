from dcim.models import (
    Device,
    DeviceRole,
    DeviceType,
    InventoryItem,
    ModuleType,
    Platform,
)
from django import forms
from netbox.forms import NetBoxModelForm
from utilities.forms.fields import (
    CommentField,
    DynamicModelChoiceField,
    DynamicModelMultipleChoiceField,
)
from utilities.forms.widgets import DatePicker
from virtualization.models import VirtualMachine

from ..models import *

__all__ = [
    'HardwareNoticeForm',
    'SoftwareNoticeForm',
    'SoftwareImageForm',
    'SoftwareImageAssociationForm',
    'ServiceProviderForm',
    'ContractForm',
]


class HardwareNoticeForm(NetBoxModelForm):
    device_type = DynamicModelChoiceField(queryset=DeviceType.objects.all(), required=False, selector=True)

    inventory_item = DynamicModelChoiceField(queryset=InventoryItem.objects.all(), required=False, selector=True)

    module_type = DynamicModelChoiceField(queryset=ModuleType.objects.all(), required=False, selector=True)

    release_date = forms.DateField(required=False, widget=DatePicker(), label='Release Date')

    end_of_sale_date = forms.DateField(required=False, widget=DatePicker(), label='End of Sale')

    end_of_support_date = forms.DateField(required=False, widget=DatePicker(), label='End of Support')

    end_of_sw_releases_date = forms.DateField(required=False, widget=DatePicker(), label='End of Software Releases')

    end_of_security_updates_date = forms.DateField(required=False, widget=DatePicker(), label='End of Security Updates')

    documentation_url = forms.URLField(required=False, label='Documentation URL')

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

    release_date = forms.DateField(required=False, widget=DatePicker(), label='Release Date')

    end_of_support_date = forms.DateField(required=False, widget=DatePicker(), label='End of Support')

    documentation_url = forms.URLField(required=False, label='Documentation URL')

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


class SoftwareImageForm(NetBoxModelForm):
    software = DynamicModelChoiceField(queryset=SoftwareNotice.objects.all(), selector=True)

    comments = CommentField()

    file_name = forms.CharField(
        required=False,
        label='File Name',
        help_text='The name of the file to be downloaded. (e.g. "image.bin")',
    )

    download_url = forms.URLField(required=False, label='Download URL', help_text='The URL to download the image from.')

    sha256_checksum = forms.CharField(
        required=False,
        label='SHA256 Checksum',
        help_text='The SHA256 checksum of the image file.',
    )

    default_image = forms.BooleanField(
        required=False,
        label='Default Image',
        help_text='The default image to be used for this software version.',
    )

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


class SoftwareImageAssociationForm(NetBoxModelForm):
    image = DynamicModelChoiceField(queryset=SoftwareImage.objects.all(), selector=True)

    comments = CommentField()

    device_types = DynamicModelMultipleChoiceField(
        queryset=DeviceType.objects.all(),
        required=False,
        label='Device Types',
        help_text='Limit this image assignment to the selected device types.',
    )

    device_roles = DynamicModelMultipleChoiceField(
        queryset=DeviceRole.objects.all(),
        required=False,
        label='Device Roles',
        help_text='Limit this image assignment to the selected device roles.',
    )

    devices = DynamicModelMultipleChoiceField(
        queryset=Device.objects.all(),
        required=False,
        label='Devices',
        help_text='Limit this image assignment to the selected devices.',
    )

    inventory_items = DynamicModelMultipleChoiceField(
        queryset=InventoryItem.objects.all(),
        required=False,
        label='Inventory Items',
        help_text='Limit this image assignment to the selected inventory items.',
    )

    virtual_machines = DynamicModelMultipleChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False,
        label='Virtual Machines',
        help_text='Limit this image assignment to the selected virtual machines.',
    )

    valid_from = forms.DateField(widget=DatePicker(), label='Valid From')

    valid_until = forms.DateField(required=False, widget=DatePicker(), label='Valid Until')

    fieldsets = (
        (None, ('image', 'description', 'tags')),
        ('Associations', ('device_types', 'device_roles', 'devices', 'inventory_items', 'virtual_machines')),
        ('Validity', ('valid_from', 'valid_until')),
    )

    class Meta:
        model = SoftwareImageAssociation
        fields = [
            'image',
            'comments',
            'device_types',
            'device_roles',
            'devices',
            'inventory_items',
            'virtual_machines',
            'description',
            'tags',
            'valid_from',
            'valid_until',
        ]


class ServiceProviderForm(NetBoxModelForm):
    class Meta:
        model = ServiceProvider
        fields = [
            'name',
            'description',
            'portal_url',
            'comments',
            'tags',
        ]


class ContractForm(NetBoxModelForm):
    service_provider = DynamicModelChoiceField(queryset=ServiceProvider.objects.all(), selector=True)

    comments = CommentField()

    start_date = forms.DateField(widget=DatePicker(), label='Start Date')

    end_date = forms.DateField(required=False, widget=DatePicker(), label='End Date')

    renewal_date = forms.DateField(required=False, widget=DatePicker(), label='Renewal Date')

    fieldsets = (
        (None, ('service_provider', 'name', 'contract_type', 'description', 'tags')),
        ('Dates', ('start_date', 'end_date')),
        ('Billing', ('cost', 'currency', 'renewal_date')),
    )

    class Meta:
        model = Contract
        fields = [
            'service_provider',
            'name',
            'contract_type',
            'start_date',
            'end_date',
            'cost',
            'currency',
            'renewal_date',
            'description',
            'comments',
            'tags',
        ]
