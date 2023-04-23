from dcim.filtersets import DeviceFilterSet
from dcim.models import Device
from dcim.tables import DeviceTable
from netbox.views import generic
from utilities.views import ViewTab, register_model_view
from virtualization.filtersets import VirtualMachineFilterSet
from virtualization.models import VirtualMachine
from virtualization.tables import VirtualMachineTable

from . import filtersets, forms, models, tables

#
# Hardware Notices
#


@register_model_view(models.HardwareNotice)
class HardwareNoticeView(generic.ObjectView):
    queryset = models.HardwareNotice.objects.all()


class HardwareNoticeListView(generic.ObjectListView):
    queryset = models.HardwareNotice.objects.all()
    table = tables.HardwareNoticeTable
    filterset = filtersets.HardwareNoticeFilterSet
    filterset_form = forms.HardwareNoticeFilterForm


@register_model_view(models.HardwareNotice, 'edit')
class HardwareNoticeEditView(generic.ObjectEditView):
    queryset = models.HardwareNotice.objects.all()
    form = forms.HardwareNoticeForm


@register_model_view(models.HardwareNotice, 'delete')
class HardwareNoticeDeleteView(generic.ObjectDeleteView):
    queryset = models.HardwareNotice.objects.all()


class HardwareNoticeBulkEditView(generic.BulkEditView):
    queryset = models.HardwareNotice.objects.all()
    table = tables.HardwareNoticeTable
    filterset = filtersets.HardwareNoticeFilterSet
    form = forms.HardwareNoticeBulkEditForm


class HardwareNoticeBulkImportView(generic.BulkImportView):
    queryset = models.HardwareNotice.objects.all()
    table = tables.HardwareNoticeTable
    model_form = forms.HardwareNoticeImportForm


class HardwareNoticeBulkDeleteView(generic.BulkDeleteView):
    queryset = models.HardwareNotice.objects.all()
    table = tables.HardwareNoticeTable
    filterset = filtersets.HardwareNoticeFilterSet


@register_model_view(models.HardwareNotice, 'devices')
class HardwareNoticeDevicesView(generic.ObjectChildrenView):
    queryset = models.HardwareNotice.objects.all()
    child_model = Device
    table = DeviceTable
    filterset = DeviceFilterSet
    template_name = 'netbox_device_lifecycle_mgmt/inc/view_tab.html'
    tab = ViewTab(label='Devices', badge=lambda obj: obj.device_count, hide_if_empty=True)

    def get_children(self, request, parent):
        qs_filter = {}

        if parent.object._meta.model_name == 'devicetype':
            qs_filter['device_type'] = parent.object
        elif parent.object._meta.model_name == 'inventoryitem':
            qs_filter['inventoryitems'] = parent.object
        elif parent.object._meta.model_name == 'moduletype':
            qs_filter['modules__module_type'] = parent.object
        else:
            return self.child_model.objects.none()

        return self.child_model.objects.restrict(request.user, 'view').filter(**qs_filter)

    def get_extra_context(self, request, instance):
        return {'table_config': f'{self.table.__name__}_config'}


#
# Software Notices
#


@register_model_view(models.SoftwareNotice)
class SoftwareNoticeView(generic.ObjectView):
    queryset = models.SoftwareNotice.objects.all()

    def get_extra_context(self, request, instance):
        image_table = tables.SoftwareImageTable(instance.images.all())
        image_table.columns.hide('software')
        image_table.configure(request=request)

        return {
            'related_images': image_table,
        }


class SoftwareNoticeListView(generic.ObjectListView):
    queryset = models.SoftwareNotice.objects.all()
    table = tables.SoftwareNoticeTable
    filterset = filtersets.SoftwareNoticeFilterSet
    filterset_form = forms.SoftwareNoticeFilterForm


@register_model_view(models.SoftwareNotice, 'edit')
class SoftwareNoticeEditView(generic.ObjectEditView):
    queryset = models.SoftwareNotice.objects.all()
    form = forms.SoftwareNoticeForm


@register_model_view(models.SoftwareNotice, 'delete')
class SoftwareNoticeDeleteView(generic.ObjectDeleteView):
    queryset = models.SoftwareNotice.objects.all()


class SoftwareNoticeBulkEditView(generic.BulkEditView):
    queryset = models.SoftwareNotice.objects.all()
    table = tables.SoftwareNoticeTable
    filterset = filtersets.SoftwareNoticeFilterSet
    form = forms.SoftwareNoticeBulkEditForm


class SoftwareNoticeBulkImportView(generic.BulkImportView):
    queryset = models.SoftwareNotice.objects.all()
    table = tables.SoftwareNoticeTable
    model_form = forms.SoftwareNoticeImportForm


class SoftwareNoticeBulkDeleteView(generic.BulkDeleteView):
    queryset = models.SoftwareNotice.objects.all()
    table = tables.SoftwareNoticeTable
    filterset = filtersets.SoftwareNoticeFilterSet


@register_model_view(models.SoftwareNotice, 'devices')
class SoftwareNoticeDevicesView(generic.ObjectChildrenView):
    queryset = models.SoftwareNotice.objects.all()
    child_model = Device
    table = DeviceTable
    filterset = DeviceFilterSet
    template_name = 'netbox_device_lifecycle_mgmt/inc/view_tab.html'
    tab = ViewTab(label='Devices', badge=lambda obj: obj.platform.devices.count(), hide_if_empty=True)

    def get_children(self, request, parent):
        return self.child_model.objects.restrict(request.user, 'view').filter(platform=parent.platform)

    def get_extra_context(self, request, instance):
        return {'table_config': f'{self.table.__name__}_config'}


@register_model_view(models.SoftwareNotice, 'virtual-machines')
class SoftwareNoticeVirtualMachinesView(generic.ObjectChildrenView):
    queryset = models.SoftwareNotice.objects.all()
    child_model = VirtualMachine
    table = VirtualMachineTable
    filterset = VirtualMachineFilterSet
    template_name = 'netbox_device_lifecycle_mgmt/inc/view_tab.html'
    tab = ViewTab(label='Virtual Machines', badge=lambda obj: obj.platform.virtual_machines.count(), hide_if_empty=True)

    def get_children(self, request, parent):
        return self.child_model.objects.restrict(request.user, 'view').filter(platform=parent.platform)

    def get_extra_context(self, request, instance):
        return {'table_config': f'{self.table.__name__}_config'}


#
# Software Images
#


@register_model_view(models.SoftwareImage)
class SoftwareImageView(generic.ObjectView):
    queryset = models.SoftwareImage.objects.all()


class SoftwareImageListView(generic.ObjectListView):
    queryset = models.SoftwareImage.objects.all()
    table = tables.SoftwareImageTable
    filterset = filtersets.SoftwareImageFilterSet
    filterset_form = forms.SoftwareImageFilterForm


@register_model_view(models.SoftwareImage, 'edit')
class SoftwareImageEditView(generic.ObjectEditView):
    queryset = models.SoftwareImage.objects.all()
    form = forms.SoftwareImageForm


@register_model_view(models.SoftwareImage, 'delete')
class SoftwareImageDeleteView(generic.ObjectDeleteView):
    queryset = models.SoftwareImage.objects.all()


class SoftwareImageBulkEditView(generic.BulkEditView):
    queryset = models.SoftwareImage.objects.all()
    table = tables.SoftwareImageTable
    filterset = filtersets.SoftwareImageFilterSet
    form = forms.SoftwareImageBulkEditForm


class SoftwareImageBulkImportView(generic.BulkImportView):
    queryset = models.SoftwareImage.objects.all()
    table = tables.SoftwareImageTable
    model_form = forms.SoftwareImageImportForm


class SoftwareImageBulkDeleteView(generic.BulkDeleteView):
    queryset = models.SoftwareImage.objects.all()
    table = tables.SoftwareImageTable
    filterset = filtersets.SoftwareImageFilterSet


@register_model_view(models.SoftwareImage, 'associations')
class SoftwareImageAssociationsView(generic.ObjectChildrenView):
    queryset = models.SoftwareImage.objects.all()
    child_model = models.SoftwareImageAssociation
    table = tables.SoftwareImageAssociationTable
    template_name = 'netbox_device_lifecycle_mgmt/inc/view_tab.html'
    tab = ViewTab(label='Associations', badge=lambda obj: obj.associations.count(), hide_if_empty=True)

    def get_children(self, request, parent):
        return self.child_model.objects.restrict(request.user, 'view').filter(image=parent)

    def get_extra_context(self, request, instance):
        return {'table_config': f'{self.table.__name__}_config'}


#
# Software Image Assignments
#


@register_model_view(models.SoftwareImageAssociation)
class SoftwareImageAssociationView(generic.ObjectView):
    queryset = models.SoftwareImageAssociation.objects.all()

    def get_extra_context(self, request, instance):
        assigned_objects = (
            ('Device Types', instance.device_types.all()),
            ('Device Roles', instance.device_roles.all()),
            ('Devices', instance.devices.all()),
            ('Inventory Items', instance.inventory_items.all()),
            ('Virtual Machines', instance.virtual_machines.all()),
        )

        return {
            'assigned_objects': assigned_objects,
        }


class SoftwareImageAssociationListView(generic.ObjectListView):
    queryset = models.SoftwareImageAssociation.objects.all()
    table = tables.SoftwareImageAssociationTable
    filterset = filtersets.SoftwareImageAssociationFilterSet
    filterset_form = forms.SoftwareImageAssociationFilterForm


@register_model_view(models.SoftwareImageAssociation, 'edit')
class SoftwareImageAssociationEditView(generic.ObjectEditView):
    queryset = models.SoftwareImageAssociation.objects.all()
    form = forms.SoftwareImageAssociationForm


@register_model_view(models.SoftwareImageAssociation, 'delete')
class SoftwareImageAssociationDeleteView(generic.ObjectDeleteView):
    queryset = models.SoftwareImageAssociation.objects.all()


class SoftwareImageAssociationBulkEditView(generic.BulkEditView):
    queryset = models.SoftwareImageAssociation.objects.all()
    table = tables.SoftwareImageAssociationTable
    filterset = filtersets.SoftwareImageAssociationFilterSet
    form = forms.SoftwareImageAssociationBulkEditForm


class SoftwareImageAssociationBulkImportView(generic.BulkImportView):
    queryset = models.SoftwareImageAssociation.objects.all()
    table = tables.SoftwareImageAssociationTable
    model_form = forms.SoftwareImageAssociationImportForm


class SoftwareImageAssociationBulkDeleteView(generic.BulkDeleteView):
    queryset = models.SoftwareImageAssociation.objects.all()
    table = tables.SoftwareImageAssociationTable
    filterset = filtersets.SoftwareImageAssociationFilterSet


#
# Service Providers
#


@register_model_view(models.ServiceProvider)
class ServiceProviderView(generic.ObjectView):
    queryset = models.ServiceProvider.objects.all()


class ServiceProviderListView(generic.ObjectListView):
    queryset = models.ServiceProvider.objects.all()
    table = tables.ServiceProviderTable
    filterset = filtersets.ServiceProviderFilterSet
    filterset_form = forms.ServiceProviderFilterForm


@register_model_view(models.ServiceProvider, 'edit')
class ServiceProviderEditView(generic.ObjectEditView):
    queryset = models.ServiceProvider.objects.all()
    form = forms.ServiceProviderForm


@register_model_view(models.ServiceProvider, 'delete')
class ServiceProviderDeleteView(generic.ObjectDeleteView):
    queryset = models.ServiceProvider.objects.all()


class ServiceProviderBulkEditView(generic.BulkEditView):
    queryset = models.ServiceProvider.objects.all()
    table = tables.ServiceProviderTable
    filterset = filtersets.ServiceProviderFilterSet
    form = forms.ServiceProviderBulkEditForm


class ServiceProviderBulkImportView(generic.BulkImportView):
    queryset = models.ServiceProvider.objects.all()
    table = tables.ServiceProviderTable
    model_form = forms.ServiceProviderImportForm


class ServiceProviderBulkDeleteView(generic.BulkDeleteView):
    queryset = models.ServiceProvider.objects.all()
    table = tables.ServiceProviderTable
    filterset = filtersets.ServiceProviderFilterSet


#
# Contracts
#


@register_model_view(models.Contract)
class ContractView(generic.ObjectView):
    queryset = models.Contract.objects.all()


class ContractListView(generic.ObjectListView):
    queryset = models.Contract.objects.all()
    table = tables.ContractTable
    filterset = filtersets.ContractFilterSet
    filterset_form = forms.ContractFilterForm


@register_model_view(models.Contract, 'edit')
class ContractEditView(generic.ObjectEditView):
    queryset = models.Contract.objects.all()
    form = forms.ContractForm


@register_model_view(models.Contract, 'delete')
class ContractDeleteView(generic.ObjectDeleteView):
    queryset = models.Contract.objects.all()


class ContractBulkEditView(generic.BulkEditView):
    queryset = models.Contract.objects.all()
    table = tables.ContractTable
    filterset = filtersets.ContractFilterSet
    form = forms.ContractBulkEditForm


class ContractBulkImportView(generic.BulkImportView):
    queryset = models.Contract.objects.all()
    table = tables.ContractTable
    model_form = forms.ContractImportForm


class ContractBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Contract.objects.all()
    table = tables.ContractTable
    filterset = filtersets.ContractFilterSet
