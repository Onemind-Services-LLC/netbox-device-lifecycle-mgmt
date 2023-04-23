import datetime

import django_filters
from dcim.models import DeviceType, InventoryItem
from django.db.models import Q
from netbox.filtersets import NetBoxModelFilterSet

from .models import *

__all__ = [
    'HardwareNoticeFilterSet',
]


class HardwareNoticeFilterSet(NetBoxModelFilterSet):
    device_type = django_filters.ModelMultipleChoiceFilter(
        field_name='device_type__slug',
        queryset=DeviceType.objects.all(),
        to_field_name='slug',
        label='Device type (slug)',
    )
    device_type_id = django_filters.ModelMultipleChoiceFilter(
        queryset=DeviceType.objects.all(),
        label='Device type (ID)',
    )

    inventory_item = django_filters.ModelMultipleChoiceFilter(
        field_name='inventory_item__name',
        queryset=InventoryItem.objects.all(),
        to_field_name='name',
        label='Inventory item (name)',
    )

    inventory_item_id = django_filters.ModelMultipleChoiceFilter(
        queryset=InventoryItem.objects.all(),
        label='Inventory item (ID)',
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
        )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset

        return queryset.filter(
            Q(description__icontains=value)
            | Q(device_type__model__icontains=value)
            | Q(inventory_item__name__icontains=value),
        )

    def filter_expired(self, queryset, name, value):
        today = datetime.date.today()
        lookup = "gte" if not value else "lt"

        qs_filter = Q(**{f"end_of_sale_date__{lookup}": today}) | Q(**{f"end_of_support_date__{lookup}": today})
        return queryset.filter(qs_filter)
