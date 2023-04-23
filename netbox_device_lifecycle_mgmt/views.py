from dcim.filtersets import DeviceFilterSet
from dcim.models import Device
from dcim.tables import DeviceTable
from netbox.views import generic
from utilities.views import ViewTab, register_model_view

from . import filtersets, forms, models, tables


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
        filter = {}

        if hasattr(parent.object, 'instances'):
            filter['pk__in'] = [i.pk for i in parent.object.instances.all()]
        elif hasattr(parent.object, 'device'):
            filter['pk'] = parent.object.device.pk

        return self.child_model.objects.restrict(request.user, 'view').filter(**filter)

    def get_extra_context(self, request, instance):
        return {'table_config': f'{self.table.__name__}_config'}
