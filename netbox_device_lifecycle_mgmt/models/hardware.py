import datetime

from django.db import models
from django.urls import reverse

from netbox.models import PrimaryModel

__all__ = ['HardwareNotice']


class HardwareNotice(PrimaryModel):
    device_type = models.ForeignKey(
        to='dcim.DeviceType',
        on_delete=models.CASCADE,
        related_name='+',
        blank=True,
        null=True,
    )
    inventory_item = models.ForeignKey(
        to='dcim.InventoryItem',
        on_delete=models.CASCADE,
        related_name='+',
        blank=True,
        null=True,
    )
    release_date = models.DateField(
        blank=True,
        null=True,
    )
    end_of_sale_date = models.DateField(
        blank=True,
        null=True,
    )
    end_of_support_date = models.DateField(
        blank=True,
        null=True,
    )
    end_of_sw_releases_date = models.DateField(
        blank=True,
        null=True,
    )
    end_of_security_updates_date = models.DateField(
        blank=True,
        null=True,
    )
    documentation_url = models.URLField(
        blank=True,
    )

    clone_fields = (
        'release_date',
        'end_of_sale_date',
        'end_of_support_date',
        'end_of_sw_releases_date',
        'end_of_security_updates_date',
        'documentation_url',
    )

    class Meta:
        verbose_name = 'Hardware Notice'
        verbose_name_plural = 'Hardware Notices'
        ordering = ['end_of_support_date', 'end_of_sale_date']
        constraints = [
            models.UniqueConstraint(
                fields=['device_type'],
                name='%(app_label)s_%(class)s_unique_device_type',
            ),
            models.UniqueConstraint(
                fields=['inventory_item'],
                name='%(app_label)s_%(class)s_unique_inventory_item',
            ),
            models.CheckConstraint(
                check=(
                        models.Q(inventory_item__isnull=True, device_type__isnull=False)
                        | models.Q(inventory_item__isnull=False, device_type__isnull=True)
                ),
                name='At least one of inventory_item or device_type must be set',
            ),
            models.CheckConstraint(
                check=(models.Q(end_of_sale_date__isnull=False) | models.Q(end_of_support_date__isnull=False)),
                name='End of sale or end of support must be set',
            ),
        ]

    def __str__(self):
        name = f'{self.device_type or self.inventory_item}'
        if self.end_of_support_date:
            name += f' (End of support: {self.end_of_support_date})'
        else:
            name += f' (End of sale: {self.end_of_sale_date})'

        return name

    def get_absolute_url(self):
        return reverse('plugins:netbox_device_lifecycle_mgmt:hardwarenotice', args=[self.pk])

    @property
    def expired(self):
        """
        Returns True if the notice has expired.
        """
        today = datetime.date.today()

        if self.end_of_support_date is not None:
            return self.end_of_support_date < today

        return self.end_of_sale_date < today
