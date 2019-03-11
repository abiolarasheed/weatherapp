# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from api.filters import WeatherFilter
from api.models import WeatherForecast
from api.serializers import WeatherForecastSerializer


class WeatherFilterListAPIView(ListAPIView):
    serializer_class = WeatherForecastSerializer
    queryset = WeatherForecast.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = WeatherFilter
