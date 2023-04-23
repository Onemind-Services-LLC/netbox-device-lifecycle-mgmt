from datetime import date

from django.contrib.contenttypes.fields import GenericRelation
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from netbox.models import PrimaryModel

from ..choices import *

__all__ = ['ServiceProvider', 'Contract']


class ServiceProvider(PrimaryModel):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    contacts = GenericRelation(
        to='tenancy.ContactAssignment',
    )

    portal_url = models.URLField(
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_device_lifecycle_mgmt:serviceprovider', args=[self.pk])


class Contract(PrimaryModel):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    service_provider = models.ForeignKey(
        to=ServiceProvider,
        on_delete=models.PROTECT,
        related_name='contracts',
    )

    contacts = GenericRelation(
        to='tenancy.ContactAssignment',
    )

    contract_number = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    start_date = models.DateField(
        blank=True,
        null=True,
    )

    end_date = models.DateField(
        blank=True,
        null=True,
    )

    renewal_date = models.DateField(
        blank=True,
        null=True,
    )

    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    currency = models.CharField(
        max_length=3,
        choices=CurrencyChoices,
        blank=True,
        null=True,
    )

    contract_type = models.CharField(
        max_length=50,
        choices=ContractTypeChoices,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_device_lifecycle_mgmt:contract', args=[self.pk])

    @property
    def expired(self):
        """
        Return True if the contract has expired.
        """
        if self.end_date:
            return self.end_date < date.today()
        return False

    def clean(self):
        super().clean()

        if self.end_date and self.start_date:
            if self.end_date <= self.start_date:
                raise ValidationError("End date must be after the start date of the contract.")

        if self.cost and not self.currency:
            raise ValidationError("Currency must be set if cost is set.")

        if self.currency and not self.cost:
            raise ValidationError("Cost must be set if currency is set.")
