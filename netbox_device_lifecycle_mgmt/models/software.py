from django.db import models
from django.urls import reverse

from netbox.models import PrimaryModel

__all__ = ['SoftwareNotice']


class SoftwareNotice(PrimaryModel):
    platform = models.ForeignKey(
        to='dcim.Platform',
        on_delete=models.CASCADE,
        related_name='+',
    )

    version = models.CharField(
        max_length=50,
    )

    release_date = models.DateField(
        blank=True,
        null=True,
    )

    end_of_support_date = models.DateField(
        blank=True,
        null=True,
    )

    documentation_url = models.URLField(
        blank=True,
        null=True,
    )

    long_term_support = models.BooleanField(
        default=False,
    )

    pre_release = models.BooleanField(
        default=False,
    )

    clone_fields = (
        'platform',
        'release_date',
        'end_of_support_date',
        'documentation_url',
        'long_term_support',
        'pre_release',
    )

    class Meta:
        ordering = ['platform', 'version', 'end_of_support_date', 'release_date']
        constraints = [
            models.UniqueConstraint(
                fields=['platform', 'version'],
                name='%(app_label)s_%(class)s_unique_software_notice',
                violation_error_message='A software notice already exists for this platform and version.',
            ),
        ]

    def __str__(self):
        return f'{self.platform} {self.version}'

    def get_absolute_url(self):
        return reverse('plugins:netbox_device_lifecycle_mgmt:softwarenotice', args=[self.pk])
