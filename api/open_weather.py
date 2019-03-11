from os import environ
from django.core.cache import cache
from requests import Response
import requests


class WeatherClient:
    """
    A simple openweathermap.org Client
    """

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    querystring = {}
    headers = {}

    def __make_request(self) -> Response:
        """
        This method makes API calls to openweathermap.org
        """
        return requests.get(
            self.base_url, headers=self.headers, params=self.querystring
        )

    def get_forecast(self, location: str = "London,UK") -> Response:
        """
        Simple method that gets forecast for given city
        """
        response = cache.get(location, None)
        if response is None:
            self.querystring.update({"q": location})
            self.headers.update({"x-api-key": environ.get("OPENWEATHERMAP")})
            response = self.__make_request()
            cache.set(location, response, 3480)
        return response
