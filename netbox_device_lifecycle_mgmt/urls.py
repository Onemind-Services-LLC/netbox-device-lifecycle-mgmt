from django.urls import include, path
from utilities.urls import get_model_urls

from . import views

app_name = 'netbox_device_lifecycle_mgmt'

urlpatterns = (
    # Hardware notices
    path('hardware-notices/', views.HardwareNoticeListView.as_view(), name='hardwarenotice_list'),
    path('hardware-notices/add/', views.HardwareNoticeEditView.as_view(), name='hardwarenotice_add'),
    path('hardware-notices/edit/', views.HardwareNoticeBulkEditView.as_view(), name='hardwarenotice_bulk_edit'),
    path('hardware-notices/import/', views.HardwareNoticeBulkImportView.as_view(), name='hardwarenotice_import'),
    path('hardware-notices/delete/', views.HardwareNoticeBulkDeleteView.as_view(), name='hardwarenotice_bulk_delete'),
    path('hardware-notices/<int:pk>/', include(get_model_urls(app_name, 'hardwarenotice'))),
    # Software notices
    path('software-notices/', views.SoftwareNoticeListView.as_view(), name='softwarenotice_list'),
    path('software-notices/add/', views.SoftwareNoticeEditView.as_view(), name='softwarenotice_add'),
    path('software-notices/edit/', views.SoftwareNoticeBulkEditView.as_view(), name='softwarenotice_bulk_edit'),
    path('software-notices/import/', views.SoftwareNoticeBulkImportView.as_view(), name='softwarenotice_import'),
    path('software-notices/delete/', views.SoftwareNoticeBulkDeleteView.as_view(), name='softwarenotice_bulk_delete'),
    path('software-notices/<int:pk>/', include(get_model_urls(app_name, 'softwarenotice'))),
    # Software Images
    path('software-images/', views.SoftwareImageListView.as_view(), name='softwareimage_list'),
    path('software-images/add/', views.SoftwareImageEditView.as_view(), name='softwareimage_add'),
    path('software-images/edit/', views.SoftwareImageBulkEditView.as_view(), name='softwareimage_bulk_edit'),
    path('software-images/import/', views.SoftwareImageBulkImportView.as_view(), name='softwareimage_import'),
    path('software-images/delete/', views.SoftwareImageBulkDeleteView.as_view(), name='softwareimage_bulk_delete'),
    path('software-images/<int:pk>/', include(get_model_urls(app_name, 'softwareimage'))),
    # Software Image Associations
    path(
        'software-image-associations/',
        views.SoftwareImageAssociationListView.as_view(),
        name='softwareimageassociation_list',
    ),
    path(
        'software-image-associations/add/',
        views.SoftwareImageAssociationEditView.as_view(),
        name='softwareimageassociation_add',
    ),
    path(
        'software-image-associations/edit/',
        views.SoftwareImageAssociationBulkEditView.as_view(),
        name='softwareimageassociation_bulk_edit',
    ),
    path(
        'software-image-associations/import/',
        views.SoftwareImageAssociationBulkImportView.as_view(),
        name='softwareimageassociation_import',
    ),
    path(
        'software-image-associations/delete/',
        views.SoftwareImageAssociationBulkDeleteView.as_view(),
        name='softwareimageassociation_bulk_delete',
    ),
    path('software-image-associations/<int:pk>/', include(get_model_urls(app_name, 'softwareimageassociation'))),
    # Service Providers
    path('service-providers/', views.ServiceProviderListView.as_view(), name='serviceprovider_list'),
    path('service-providers/add/', views.ServiceProviderEditView.as_view(), name='serviceprovider_add'),
    path('service-providers/edit/', views.ServiceProviderBulkEditView.as_view(), name='serviceprovider_bulk_edit'),
    path('service-providers/import/', views.ServiceProviderBulkImportView.as_view(), name='serviceprovider_import'),
    path(
        'service-providers/delete/',
        views.ServiceProviderBulkDeleteView.as_view(),
        name='serviceprovider_bulk_delete',
    ),
    path('service-providers/<int:pk>/', include(get_model_urls(app_name, 'serviceprovider'))),
)
