import graphene
from netbox.graphql.fields import ObjectField, ObjectListField

from .types import *


class NetBoxDeviceLifecycleMgmtQuery(graphene.ObjectType):
    hardware_notice = ObjectField(HardwareNoticeType)
    hardware_notice_list = ObjectListField(HardwareNoticeType)

    software_notice = ObjectField(SoftwareNoticeType)
    software_notice_list = ObjectListField(SoftwareNoticeType)

    software_image = ObjectField(SoftwareImageType)
    software_image_list = ObjectListField(SoftwareImageType)

    software_image_association = ObjectField(SoftwareImageAssociationType)
    software_image_association_list = ObjectListField(SoftwareImageAssociationType)

    service_provider = ObjectField(ServiceProviderType)
    service_provider_list = ObjectListField(ServiceProviderType)
