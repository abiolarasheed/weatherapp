import json

from rest_framework import serializers

from api.models import WeatherForecast


class WeatherForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherForecast
        fields = "__all__"

    @staticmethod
    def get_data(obj):
        return json.loads(obj.data)
