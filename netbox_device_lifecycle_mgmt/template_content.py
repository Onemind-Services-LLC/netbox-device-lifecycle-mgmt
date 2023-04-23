from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from extras.plugins import PluginTemplateExtension

from .models import HardwareNotice


class GeneralNoticeExtension(PluginTemplateExtension):
    def right_page(self):
        filters = {
            'object_type': ContentType.objects.get_for_model(self.context['object']),
            'object_id': self.context['object'].id,
        }

        if instance := HardwareNotice.objects.filter(**filters).first():
            return self.render(
                'netbox_device_lifecycle_mgmt/inc/general_notice.html',
                extra_context={'object': instance},
            )
        return ''


class DeviceTypeHardwareNoticeExtension(GeneralNoticeExtension):
    model = 'dcim.devicetype'


class InventoryItemHardwareNoticeExtension(GeneralNoticeExtension):
    model = 'dcim.inventoryitem'


class DeviceHardwareNoticeExtension(PluginTemplateExtension):
    model = 'dcim.device'

    def left_page(self):
        qs_filters = Q(
            object_type=ContentType.objects.get(app_label='dcim', model='devicetype'),
            object_id=self.context['object'].device_type.id,
        ) | Q(
            object_type=ContentType.objects.get(app_label='dcim', model='inventoryitem'),
            object_id__in=self.context['object'].inventoryitems.values_list('id', flat=True),
        )

        return self.render(
            'netbox_device_lifecycle_mgmt/inc/device_notice.html',
            extra_context={
                'objects': HardwareNotice.objects.filter(qs_filters),
            },
        )


template_extensions = [
    DeviceTypeHardwareNoticeExtension,
    InventoryItemHardwareNoticeExtension,
    DeviceHardwareNoticeExtension,
]
