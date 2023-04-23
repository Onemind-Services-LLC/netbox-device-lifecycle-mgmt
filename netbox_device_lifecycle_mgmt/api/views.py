from netbox.api.viewsets import NetBoxModelViewSet

from ..models import *
from .serializers import *

__all__ = ['HardwareNoticeViewSet']


class HardwareNoticeViewSet(NetBoxModelViewSet):
    queryset = HardwareNotice.objects.all()
    serializer_class = HardwareNoticeSerializer
