from netbox.forms import NetBoxModelBulkEditForm

from ..models import *

__all__ = [
    'HardwareNoticeBulkEditForm',
    'SoftwareNoticeBulkEditForm',
    'SoftwareImageBulkEditForm',
    'SoftwareImageAssociationBulkEditForm',
    'ServiceProviderBulkEditForm',
]


class HardwareNoticeBulkEditForm(NetBoxModelBulkEditForm):
    model = HardwareNotice


class SoftwareNoticeBulkEditForm(NetBoxModelBulkEditForm):
    model = SoftwareNotice


class SoftwareImageBulkEditForm(NetBoxModelBulkEditForm):
    model = SoftwareImage


class SoftwareImageAssociationBulkEditForm(NetBoxModelBulkEditForm):
    model = SoftwareImageAssociation


class ServiceProviderBulkEditForm(NetBoxModelBulkEditForm):
    model = ServiceProvider
