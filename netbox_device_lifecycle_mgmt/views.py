from dcim.models import Device
from dcim.tables import DeviceTable
from netbox.views import generic
from utilities.views import ViewTab, register_model_view

from . import forms, models, tables


@register_model_view(models.HardwareNotice)
class HardwareNoticeView(generic.ObjectView):
    queryset = models.HardwareNotice.objects.all()


class HardwareNoticeListView(generic.ObjectListView):
    queryset = models.HardwareNotice.objects.all()
    table = tables.HardwareNoticeTable


@register_model_view(models.HardwareNotice, 'edit')
class HardwareNoticeEditView(generic.ObjectEditView):
    queryset = models.HardwareNotice.objects.all()
    form = forms.HardwareNoticeForm


@register_model_view(models.HardwareNotice, 'delete')
class HardwareNoticeDeleteView(generic.ObjectDeleteView):
    queryset = models.HardwareNotice.objects.all()


@register_model_view(models.HardwareNotice, 'devices')
class HardwareNoticeDevicesView(generic.ObjectChildrenView):
    queryset = models.HardwareNotice.objects.all()
    child_model = Device
    table = DeviceTable
    template_name = 'netbox_device_lifecycle_mgmt/inc/view_tab.html'
    tab = ViewTab(label='Devices', hide_if_empty=True)

    def get_children(self, request, parent):
        print('parent.device_type: ', parent.device_type)

        if parent.device_type:
            return self.child_model.objects.restrict(request.user, 'view').filter(device_type=parent.device_type)

        if parent.inventory_item:
            return self.child_model.objects.restrict(request.user, 'view').filter(inventoryitems=parent.inventory_item)

        return self.child_model.objects.none()

    def get_extra_context(self, request, instance):
        return {'table_config': f'{self.table.__name__}_config'}
