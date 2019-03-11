# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models


class WeatherForecast(models.Model):
    data = models.TextField()
    city = models.CharField(max_length=1100)
    datetime = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.city} {self.datetime}"
