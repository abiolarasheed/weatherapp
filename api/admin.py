from django.contrib import admin

# Register your models here.
from api.models import WeatherForecast

admin.register(WeatherForecast)
