# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import django_filters
from django_filters import DateTimeFromToRangeFilter
from django_filters.widgets import RangeWidget

from api.models import WeatherForecast


class WeatherFilter(django_filters.rest_framework.FilterSet):
    datetime = DateTimeFromToRangeFilter(
        lookup_expr=("icontains"), widget=RangeWidget(attrs={"type": "datetime-local"})
    )

    class Meta:
        model = WeatherForecast
        fields = ("datetime",)
