from dcim.models import Device, DeviceRole, DeviceType, InventoryItem, Platform
from django import forms
from netbox.forms import NetBoxModelFilterSetForm
from utilities.forms.fields import DynamicModelMultipleChoiceField, TagFilterField
from utilities.forms.widgets import DatePicker
from virtualization.models import VirtualMachine

from ..models import *

__all__ = [
    'HardwareNoticeFilterForm',
    'SoftwareNoticeFilterForm',
    'SoftwareImageFilterForm',
    'SoftwareImageAssociationFilterForm',
]


class HardwareNoticeFilterForm(NetBoxModelFilterSetForm):
    model = HardwareNotice

    fieldsets = (
        (None, ('q', 'filter_id', 'tag')),
        ('Release Date', ('release_date', 'release_date__before', 'release_date__after')),
        ('End of Sale', ('end_of_sale', 'end_of_sale__before', 'end_of_sale__after')),
        ('End of Support', ('end_of_support', 'end_of_support__before', 'end_of_support__after')),
        ('End of Software Releases', ('end_of_sw_releases', 'end_of_sw_releases__before', 'end_of_sw_releases__after')),
        (
            'End of Security Updates',
            ('end_of_security_updates', 'end_of_security_updates__before', 'end_of_security_updates__after'),
        ),
    )

    release_date = forms.DateField(required=False, label='Release Date', widget=DatePicker())

    release_date__before = forms.DateField(required=False, label='Release Date (Before)', widget=DatePicker())

    release_date__after = forms.DateField(required=False, label='Release Date (After)', widget=DatePicker())

    end_of_sale = forms.DateField(required=False, label='End of Sale', widget=DatePicker())

    end_of_sale__before = forms.DateField(required=False, label='End of Sale (Before)', widget=DatePicker())

    end_of_sale__after = forms.DateField(required=False, label='End of Sale (After)', widget=DatePicker())

    end_of_support = forms.DateField(required=False, label='End of Support', widget=DatePicker())

    end_of_support__before = forms.DateField(required=False, label='End of Support (Before)', widget=DatePicker())

    end_of_support__after = forms.DateField(required=False, label='End of Support (After)', widget=DatePicker())

    end_of_sw_releases = forms.DateField(required=False, label='End of Software Releases', widget=DatePicker())

    end_of_sw_releases__before = forms.DateField(
        required=False,
        label='End of Software Releases (Before)',
        widget=DatePicker(),
    )

    end_of_sw_releases__after = forms.DateField(
        required=False,
        label='End of Software Releases (After)',
        widget=DatePicker(),
    )

    end_of_security_updates = forms.DateField(required=False, label='End of Security Updates', widget=DatePicker())

    end_of_security_updates__before = forms.DateField(
        required=False,
        label='End of Security Updates (Before)',
        widget=DatePicker(),
    )

    end_of_security_updates__after = forms.DateField(
        required=False,
        label='End of Security Updates (After)',
        widget=DatePicker(),
    )

    tag = TagFilterField(model)


class SoftwareNoticeFilterForm(NetBoxModelFilterSetForm):
    model = SoftwareNotice

    fieldsets = (
        (None, ('q', 'filter_id', 'tag')),
        ('Platform', ('device_platform', 'version')),
        ('Release Date', ('release_date', 'release_date__before', 'release_date__after')),
        ('End of Support', ('end_of_support', 'end_of_support__before', 'end_of_support__after')),
        ('Attributes', ('documentation_url', 'long_term_support', 'pre_release')),
    )

    device_platform = DynamicModelMultipleChoiceField(
        queryset=Platform.objects.all(),
        required=False,
        label='Device Platform',
    )

    version = forms.CharField(required=False)

    release_date = forms.DateField(required=False, label='Release Date', widget=DatePicker())

    release_date__before = forms.DateField(required=False, label='Release Date (Before)', widget=DatePicker())

    release_date__after = forms.DateField(required=False, label='Release Date (After)', widget=DatePicker())

    end_of_support = forms.DateField(required=False, label='End of Support', widget=DatePicker())

    end_of_support__before = forms.DateField(required=False, label='End of Support (Before)', widget=DatePicker())

    end_of_support__after = forms.DateField(required=False, label='End of Support (After)', widget=DatePicker())

    documentation_url = forms.URLField(required=False, label='Documentation URL')

    long_term_support = forms.BooleanField(required=False, label='Long Term Support')

    pre_release = forms.BooleanField(required=False, label='Pre Release')

    tag = TagFilterField(model)


class SoftwareImageFilterForm(NetBoxModelFilterSetForm):
    model = SoftwareImage

    fieldsets = (
        (None, ('q', 'filter_id', 'tag')),
        ('Software', ('software', 'default_image')),
    )

    software = DynamicModelMultipleChoiceField(
        queryset=SoftwareNotice.objects.all(),
        required=False,
        label='Software',
    )

    default_image = forms.BooleanField(required=False, label='Default Image')

    tag = TagFilterField(model)


class SoftwareImageAssociationFilterForm(NetBoxModelFilterSetForm):
    model = SoftwareImageAssociation

    fieldsets = (
        (None, ('q', 'filter_id', 'tag')),
        ('Software', ('image',)),
        ('Device', ('device_types', 'device_roles', 'devices')),
        ('Inventory', ('inventory_items',)),
        ('Virtualization', ('virtual_machines',)),
        ('Valid From', ('valid_from', 'valid_from__before', 'valid_from__after')),
        ('Valid Until', ('valid_until', 'valid_until__before', 'valid_until__after')),
    )

    image = DynamicModelMultipleChoiceField(
        queryset=SoftwareImage.objects.all(),
        required=False,
        label='Image',
    )

    device_types = DynamicModelMultipleChoiceField(
        queryset=DeviceType.objects.all(),
        required=False,
        label='Device Types',
    )

    device_roles = DynamicModelMultipleChoiceField(
        queryset=DeviceRole.objects.all(),
        required=False,
        label='Device Roles',
    )

    devices = DynamicModelMultipleChoiceField(
        queryset=Device.objects.all(),
        required=False,
    )

    inventory_items = DynamicModelMultipleChoiceField(
        queryset=InventoryItem.objects.all(),
        required=False,
        label='Inventory Items',
    )

    virtual_machines = DynamicModelMultipleChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False,
        label='Virtual Machines',
    )

    valid_from = forms.DateField(required=False, label='Valid From', widget=DatePicker())

    valid_from__before = forms.DateField(required=False, label='Valid From (Before)', widget=DatePicker())

    valid_from__after = forms.DateField(required=False, label='Valid From (After)', widget=DatePicker())

    valid_until = forms.DateField(required=False, label='Valid To', widget=DatePicker())

    valid_until__before = forms.DateField(required=False, label='Valid To (Before)', widget=DatePicker())

    valid_until__after = forms.DateField(required=False, label='Valid To (After)', widget=DatePicker())

    tag = TagFilterField(model)
