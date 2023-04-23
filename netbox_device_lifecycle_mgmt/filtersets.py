import datetime

import django_filters
from django.db.models import Q

from dcim.models import Platform
from netbox.filtersets import NetBoxModelFilterSet
from utilities.filters import ContentTypeFilter
from .models import *

__all__ = [
    'HardwareNoticeFilterSet',
    'SoftwareNoticeFilterSet',
    'SoftwareImageFilterSet',
]


class HardwareNoticeFilterSet(NetBoxModelFilterSet):
    object_type = ContentTypeFilter()

    object = django_filters.BooleanFilter(
        method='_has_assigned_object',
        field_name='object',
        label='Has assigned object?',
    )

    documentation_url = django_filters.CharFilter(
        lookup_expr='icontains',
    )

    release_date = django_filters.DateFilter(
        field_name='release_date',
        lookup_expr='exact',
        label='Release date',
    )

    release_date__before = django_filters.DateFilter(
        field_name='release_date',
        lookup_expr='lte',
        label='Release date (before)',
    )

    release_date__after = django_filters.DateFilter(
        field_name='release_date',
        lookup_expr='gte',
        label='Release date (after)',
    )

    end_of_sale = django_filters.DateFilter(
        field_name='end_of_sale_date',
        lookup_expr='exact',
        label='End of sale',
    )

    end_of_sale__before = django_filters.DateFilter(
        field_name='end_of_sale_date',
        lookup_expr='lte',
        label='End of sale (before)',
    )

    end_of_sale__after = django_filters.DateFilter(
        field_name='end_of_sale_date',
        lookup_expr='gte',
        label='End of sale (after)',
    )

    end_of_support = django_filters.DateFilter(
        field_name='end_of_support_date',
        lookup_expr='exact',
        label='End of support',
    )

    end_of_support__before = django_filters.DateFilter(
        field_name='end_of_support_date',
        lookup_expr='lte',
        label='End of support (before)',
    )

    end_of_support__after = django_filters.DateFilter(
        field_name='end_of_support_date',
        lookup_expr='gte',
        label='End of support (after)',
    )

    end_of_sw_releases = django_filters.DateFilter(
        field_name='end_of_sw_releases_date',
        lookup_expr='exact',
        label='End of software releases',
    )

    end_of_sw_releases__before = django_filters.DateFilter(
        field_name='end_of_sw_releases_date',
        lookup_expr='lte',
        label='End of software releases (before)',
    )

    end_of_sw_releases__after = django_filters.DateFilter(
        field_name='end_of_sw_releases_date',
        lookup_expr='gte',
        label='End of software releases (after)',
    )

    end_of_security_updates = django_filters.DateFilter(
        field_name='end_of_security_updates_date',
        lookup_expr='exact',
        label='End of security updates',
    )

    end_of_security_updates__before = django_filters.DateFilter(
        field_name='end_of_security_updates_date',
        lookup_expr='lte',
        label='End of security updates (before)',
    )

    end_of_security_updates__after = django_filters.DateFilter(
        field_name='end_of_security_updates_date',
        lookup_expr='gte',
        label='End of security updates (after)',
    )

    expired = django_filters.BooleanFilter(
        method='filter_expired',
        label='Expired',
    )

    class Meta:
        model = HardwareNotice
        fields = (
            'id',
            'description',
            'object_type',
            'object_id',
        )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset

        return queryset.filter(description__icontains=value)

    def filter_expired(self, queryset, name, value):
        today = datetime.date.today()
        lookup = "gte" if not value else "lt"

        qs_filter = Q(**{f"end_of_sale_date__{lookup}": today}) | Q(**{f"end_of_support_date__{lookup}": today})
        return queryset.filter(qs_filter)


class SoftwareNoticeFilterSet(NetBoxModelFilterSet):
    platform_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Platform.objects.all(),
        label='Platform'
    )
    platform = django_filters.ModelMultipleChoiceFilter(
        field_name='platform__slug',
        queryset=Platform.objects.all(),
        to_field_name='slug',
        label='Platform (slug)'
    )

    documentation_url = django_filters.CharFilter(
        lookup_expr='icontains',
    )

    release_date = django_filters.DateFilter(
        field_name='release_date',
        lookup_expr='exact',
        label='Release date',
    )

    release_date__before = django_filters.DateFilter(
        field_name='release_date',
        lookup_expr='lte',
        label='Release date (before)',
    )

    release_date__after = django_filters.DateFilter(
        field_name='release_date',
        lookup_expr='gte',
        label='Release date (after)',
    )

    end_of_support = django_filters.DateFilter(
        field_name='end_of_support_date',
        lookup_expr='exact',
        label='End of support',
    )

    end_of_support__before = django_filters.DateFilter(
        field_name='end_of_support_date',
        lookup_expr='lte',
        label='End of support (before)',
    )

    end_of_support__after = django_filters.DateFilter(
        field_name='end_of_support_date',
        lookup_expr='gte',
        label='End of support (after)',
    )

    class Meta:
        model = SoftwareNotice
        fields = (
            'id',
            'description',
            'platform_id',
            'platform',
        )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset

        return queryset.filter(description__icontains=value)


class SoftwareImageFilterSet(NetBoxModelFilterSet):
    software_id = django_filters.ModelMultipleChoiceFilter(
        queryset=SoftwareNotice.objects.all(),
        label='Software'
    )

    software = django_filters.ModelMultipleChoiceFilter(
        #field_name='software__name',
        queryset=SoftwareNotice.objects.all(),
        to_field_name='_name',
        label='Software (Name)'
    )

    default_image = django_filters.BooleanFilter(
        label='Default image',
    )

    class Meta:
        model = SoftwareImage
        fields = (
            'id',
            'software_id',
            'software',
        )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset

        return queryset.filter(
            Q(software__name__icontains=value) |
            Q(software__description__icontains=value)
        )
