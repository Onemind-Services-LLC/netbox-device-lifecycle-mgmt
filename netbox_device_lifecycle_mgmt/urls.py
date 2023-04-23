from django.urls import include, path
from utilities.urls import get_model_urls

from . import views

app_name = 'netbox_device_lifecycle_mgmt'

urlpatterns = (
    # HardwareLCM
    path('hardware-notices/', views.HardwareNoticeListView.as_view(), name='hardwarenotice_list'),
    path('hardware-notices/add/', views.HardwareNoticeEditView.as_view(), name='hardwarenotice_add'),
    path('hardware-notices/edit/', views.HardwareNoticeBulkEditView.as_view(), name='hardwarenotice_bulk_edit'),
    path('hardware-notices/import/', views.HardwareNoticeBulkImportView.as_view(), name='hardwarenotice_import'),
    path('hardware-notices/delete/', views.HardwareNoticeBulkDeleteView.as_view(), name='hardwarenotice_bulk_delete'),
    path('hardware-notices/<int:pk>/', include(get_model_urls(app_name, 'hardwarenotice'))),
)
