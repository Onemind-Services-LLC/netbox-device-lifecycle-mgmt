from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse
from netbox.models import PrimaryModel

__all__ = ['ServiceProvider']


class ServiceProvider(PrimaryModel):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    contacts = GenericRelation(
        to='tenancy.ContactAssignment',
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_device_lifecycle_mgmt:serviceprovider', args=[self.pk])
