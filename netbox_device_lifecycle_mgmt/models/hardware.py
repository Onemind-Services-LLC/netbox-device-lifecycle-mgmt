import datetime

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from netbox.models import PrimaryModel

__all__ = ['HardwareNotice']


class HardwareNotice(PrimaryModel):
    object_type = models.ForeignKey(to='contenttypes.ContentType', on_delete=models.CASCADE, related_name='+')
    object_id = models.PositiveBigIntegerField()
    object = GenericForeignKey(ct_field='object_type', fk_field='object_id')

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
                fields=['object_type', 'object_id'],
                name='%(app_label)s_%(class)s_unique_object',
                violation_error_message='A hardware notice already exists for this object.',
            ),
            models.CheckConstraint(
                check=(models.Q(end_of_sale_date__isnull=False) | models.Q(end_of_support_date__isnull=False)),
                name='%(app_label)s_%(class)s_end_of_sale_or_support',
                violation_error_message='Either end of sale or end of support must be set.',
            ),
        ]

    def __str__(self):
        name = f'{self.object}'
        if self.end_of_support_date:
            name += f' (End of support: {self.end_of_support_date})'
        else:
            name += f' (End of sale: {self.end_of_sale_date})'

        name = f'{self.object_type.model_class()._meta.verbose_name.title()}: {name}'
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

    @property
    def device_count(self):
        """
        Returns the number of devices associated with this notice.
        """
        if hasattr(self.object, 'instances'):
            return self.object.instances.count()
        elif hasattr(self.object, 'device'):
            return 1
        return 0
