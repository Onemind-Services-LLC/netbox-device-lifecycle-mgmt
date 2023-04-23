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
        return self.child_model.objects.restrict(request.user, 'view').filter(
            platform=parent.platform
        )

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
        return self.child_model.objects.restrict(request.user, 'view').filter(
            platform=parent.platform
        )

    def get_extra_context(self, request, instance):
        return {'table_config': f'{self.table.__name__}_config'}
