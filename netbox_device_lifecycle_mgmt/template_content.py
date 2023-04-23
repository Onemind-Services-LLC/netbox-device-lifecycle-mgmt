from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from extras.plugins import PluginTemplateExtension

from .models import *


class HardwareGeneralNoticeExtension(PluginTemplateExtension):
    def right_page(self):
        filters = {
            'object_type': ContentType.objects.get_for_model(self.context['object']),
            'object_id': self.context['object'].id,
        }

        if instance := HardwareNotice.objects.filter(**filters).first():
            return self.render(
                'netbox_device_lifecycle_mgmt/inc/hardware_general_notice.html',
                extra_context={'object': instance},
            )
        return ''


class DeviceTypeHardwareNoticeExtensionHardware(HardwareGeneralNoticeExtension):
    model = 'dcim.devicetype'


class InventoryItemHardwareNoticeExtensionHardware(HardwareGeneralNoticeExtension):
    model = 'dcim.inventoryitem'


class ModuleTypeHardwareNoticeExtensionHardware(HardwareGeneralNoticeExtension):
    model = 'dcim.moduletype'


class DeviceHardwareNoticeExtension(PluginTemplateExtension):
    model = 'dcim.device'

    def left_page(self):
        qs_filters = (
            Q(
                object_type=ContentType.objects.get(app_label='dcim', model='devicetype'),
                object_id=self.context['object'].device_type.id,
            )
            | Q(
                object_type=ContentType.objects.get(app_label='dcim', model='inventoryitem'),
                object_id__in=self.context['object'].inventoryitems.values_list('id', flat=True),
            )
            | Q(
                object_type=ContentType.objects.get(app_label='dcim', model='moduletype'),
                object_id__in=self.context['object'].modules.values_list('module_type_id', flat=True),
            )
        )

        return self.render(
            'netbox_device_lifecycle_mgmt/inc/device_hardware_notice.html',
            extra_context={
                'objects': HardwareNotice.objects.filter(qs_filters),
            },
        )


class SoftwareGeneralNoticeExtension(PluginTemplateExtension):
    model = 'dcim.platform'

    def right_page(self):
        if instance := SoftwareNotice.objects.filter(platform=self.context['object']).first():
            return self.render(
                'netbox_device_lifecycle_mgmt/inc/software_general_notice.html',
                extra_context={'object': instance},
            )
        return ''


class DeviceVmSoftwareNoticeExtension(PluginTemplateExtension):
    def left_page(self):
        return self.render(
            'netbox_device_lifecycle_mgmt/inc/device_vm_software_notice.html',
            extra_context={'objects': SoftwareNotice.objects.filter(platform=self.context['object'].platform)},
        )


class DeviceSoftwareNoticeExtension(DeviceVmSoftwareNoticeExtension):
    model = 'dcim.device'


class VirtualMachineSoftwareNoticeExtension(DeviceVmSoftwareNoticeExtension):
    model = 'virtualization.virtualmachine'


template_extensions = [
    DeviceTypeHardwareNoticeExtensionHardware,
    InventoryItemHardwareNoticeExtensionHardware,
    DeviceHardwareNoticeExtension,
    ModuleTypeHardwareNoticeExtensionHardware,
    SoftwareGeneralNoticeExtension,
    DeviceSoftwareNoticeExtension,
    VirtualMachineSoftwareNoticeExtension,
]
