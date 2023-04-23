from netbox.api.viewsets import NetBoxModelViewSet
from .serializers import *
from ..filtersets import *
from ..models import *


class HardwareNoticeViewSet(NetBoxModelViewSet):
    queryset = HardwareNotice.objects.all()
    serializer_class = HardwareNoticeSerializer
    filterset_class = HardwareNoticeFilterSet


class SoftwareNoticeViewSet(NetBoxModelViewSet):
    queryset = SoftwareNotice.objects.all()
    serializer_class = SoftwareNoticeSerializer
    filterset_class = SoftwareNoticeFilterSet
