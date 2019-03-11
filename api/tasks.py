import json

from celery import shared_task
from django.utils import timezone

from api.models import WeatherForecast
from api.open_weather import WeatherClient


@shared_task
def fetch_weather_forecast() -> None:
    datetime = timezone.now()
    client = WeatherClient()
    response = client.get_forecast()
    WeatherForecast.objects.create(datetime=datetime, data=json.dumps(response.json()))
