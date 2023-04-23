from django.urls import include, path
from utilities.urls import get_model_urls

from . import views

app_name = 'netbox_device_lifecycle_mgmt'

urlpatterns = (
    # HardwareLCM
    path('hardware-notices/', views.HardwareNoticeListView.as_view(), name='hardwarenotice_list'),
    path('hardware-notices/add/', views.HardwareNoticeEditView.as_view(), name='hardwarenotice_add'),
    path('hardware-notices/<int:pk>/', include(get_model_urls(app_name, 'hardwarenotice'))),
)
