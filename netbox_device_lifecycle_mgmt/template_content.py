from django.db.models import Q
from extras.plugins import PluginTemplateExtension

from .models import HardwareNotice


class GeneralNoticeExtension(PluginTemplateExtension):
    def right_page(self):
        if self.model == 'dcim.devicetype':
            filters = {'device_type': self.context['object']}
        elif self.model == 'dcim.inventoryitem':
            filters = {'inventory_item': self.context['object']}
        else:
            filters = {}

        if filters:
            return self.render(
                'netbox_device_lifecycle_mgmt/inc/general_notice.html',
                extra_context={'object': HardwareNotice.objects.filter(**filters).first()},
            )
        return ''


class DeviceTypeHardwareNoticeExtension(GeneralNoticeExtension):
    model = 'dcim.devicetype'


class InventoryItemHardwareNoticeExtension(GeneralNoticeExtension):
    model = 'dcim.inventoryitem'


class DeviceHardwareNoticeExtension(PluginTemplateExtension):
    model = 'dcim.device'

    def left_page(self):
        obj = self.context['object']

        return self.render(
            'netbox_device_lifecycle_mgmt/inc/device_notice.html',
            extra_context={
                'objects': HardwareNotice.objects.filter(
                    Q(device_type=obj.device_type) | Q(inventory_item__in=[i.pk for i in obj.inventoryitems.all()]),
                ),
            },
        )


template_extensions = [
    DeviceTypeHardwareNoticeExtension,
    InventoryItemHardwareNoticeExtension,
    DeviceHardwareNoticeExtension,
]
