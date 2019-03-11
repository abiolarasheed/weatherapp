import json
from typing import Dict, Any

from rest_framework import serializers

from api.models import WeatherForecast


class WeatherForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherForecast
        fields = "__all__"

    @staticmethod
    def get_data(obj) -> Dict[Any, Any]:
        return json.loads(obj.data)
