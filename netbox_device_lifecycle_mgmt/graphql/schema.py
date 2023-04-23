import graphene
from netbox.graphql.fields import ObjectField, ObjectListField

from .types import *


class NetBoxDeviceLifecycleMgmtQuery(graphene.ObjectType):
    hardware_notice = ObjectField(HardwareNoticeType)
    hardware_notice_list = ObjectListField(HardwareNoticeType)
