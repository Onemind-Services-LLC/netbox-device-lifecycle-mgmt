from netbox.api.viewsets import NetBoxModelViewSet

from ..filtersets import *
from ..models import *
from .serializers import *


class HardwareNoticeViewSet(NetBoxModelViewSet):
    queryset = HardwareNotice.objects.all()
    serializer_class = HardwareNoticeSerializer
    filterset_class = HardwareNoticeFilterSet


class SoftwareNoticeViewSet(NetBoxModelViewSet):
    queryset = SoftwareNotice.objects.all()
    serializer_class = SoftwareNoticeSerializer
    filterset_class = SoftwareNoticeFilterSet


class SoftwareImageViewSet(NetBoxModelViewSet):
    queryset = SoftwareImage.objects.all()
    serializer_class = SoftwareImageSerializer
    filterset_class = SoftwareImageFilterSet


class SoftwareImageAssociationViewSet(NetBoxModelViewSet):
    queryset = SoftwareImageAssociation.objects.all()
    serializer_class = SoftwareImageAssociationSerializer
    filterset_class = SoftwareImageAssociationFilterSet


class ServiceProviderViewSet(NetBoxModelViewSet):
    queryset = ServiceProvider.objects.all()
    serializer_class = ServiceProviderSerializer
    filterset_class = ServiceProviderFilterSet
