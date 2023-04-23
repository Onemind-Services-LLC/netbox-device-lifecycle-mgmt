from netbox.api.routers import NetBoxRouter

from . import views

app_name = 'netbox_device_lifecycle_mgmt'

router = NetBoxRouter()
router.register('hardware-notices', views.HardwareNoticeViewSet)
router.register('software-notices', views.SoftwareNoticeViewSet)

urlpatterns = router.urls
