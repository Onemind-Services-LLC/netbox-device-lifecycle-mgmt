from datetime import date

from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from netbox.models import PrimaryModel

__all__ = ['SoftwareNotice', 'SoftwareImage', 'SoftwareImageAssociation']


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

    # Cached fields
    _name = models.CharField(
        max_length=255,
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

    def save(self, *args, **kwargs):
        self._name = str(self.platform.name)
        super().save(*args, **kwargs)

    @property
    def expired(self):
        """
        Return True if the software notice is expired.
        """
        return self.end_of_support_date and self.end_of_support_date < date.today()

    @property
    def name(self):
        """
        Return the name of the software notice.
        """
        return self._name


class SoftwareImage(PrimaryModel):
    software = models.ForeignKey(
        to='SoftwareNotice',
        on_delete=models.CASCADE,
        related_name='images',
    )

    file_name = models.CharField(
        max_length=255,
    )

    download_url = models.URLField(blank=True)

    sha256_checksum = models.CharField(
        max_length=64,
        blank=True,
    )

    default_image = models.BooleanField(
        default=False,
    )

    clone_fields = (
        'software',
        'default_image',
    )

    prerequisite_models = ('netbox_device_lifecycle_mgmt.softwarenotice',)

    class Meta:
        ordering = ['software', 'default_image', 'file_name']
        constraints = [
            models.UniqueConstraint(
                fields=['software', 'file_name'],
                name='%(app_label)s_%(class)s_unique_software_image',
                violation_error_message='A software image already exists for this software and file name.',
            ),
        ]

    def __str__(self):
        return self.file_name

    def get_absolute_url(self):
        return reverse('plugins:netbox_device_lifecycle_mgmt:softwareimage', args=[self.pk])

    def clean(self):
        super().clean()

        if self.sha256_checksum and len(self.sha256_checksum) != 64:
            raise ValidationError(
                {
                    'sha256_checksum': 'Invalid SHA256 checksum.',
                },
            )

    def save(self, *args, **kwargs):
        if self.default_image:
            self.software.images.exclude(pk=self.pk).update(default_image=False)
        super().save(*args, **kwargs)


class SoftwareImageAssociation(PrimaryModel):
    image = models.ForeignKey(
        to='SoftwareImage',
        on_delete=models.CASCADE,
        related_name='+',
    )

    device_types = models.ManyToManyField(
        to='dcim.DeviceType',
        related_name='+',
    )

    device_roles = models.ManyToManyField(
        to='dcim.DeviceRole',
        related_name='+',
    )

    devices = models.ManyToManyField(
        to='dcim.Device',
        related_name='+',
    )

    inventory_items = models.ManyToManyField(
        to='dcim.InventoryItem',
        related_name='+',
    )

    virtual_machines = models.ManyToManyField(
        to='virtualization.VirtualMachine',
        related_name='+',
    )

    valid_from = models.DateField()

    valid_until = models.DateField(
        blank=True,
        null=True,
    )

    class Meta:
        ordering = [
            'image',
            'valid_from',
        ]

    def __str__(self):
        return f'{self.image} - Valid From: {self.valid_from}'

    @property
    def valid(self):
        """
        Return True if the assignment is valid.
        """
        today = date.today()
        return self.valid_from <= today and (self.valid_until is None or self.valid_until >= today)

    def get_absolute_url(self):
        return reverse('plugins:netbox_device_lifecycle_mgmt:softwareimageassociation', args=[self.pk])
