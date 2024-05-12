import json
from django.shortcuts import render
import requests
from rest_framework.views import APIView
from django.http import HttpResponseBadRequest, JsonResponse
from weatherApp.serializers import WeatherParametersSerializer


class WeatherParameters(APIView):
    def get(self, request, latitude, longitude):
        serializer = WeatherParametersSerializer(data={'latitude': latitude, 'longitude': longitude})
        if serializer.is_valid():
            latitude = serializer.validated_data['latitude']
            longitude = serializer.validated_data['longitude']
            api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weather_code,temperature_2m_max,temperature_2m_min,daylight_duration"
            response = requests.get(api_url)
            data = response.json()
            daylight_durations = data['daily']['daylight_duration']
            power_installation = 2.5
            effectiveness_panel = 0.2
            data['daily']['generated_energy_kwh'] = []
            for index,key in enumerate(daylight_durations):
                generated_energy_kwh = power_installation * (key / 3600) * effectiveness_panel
                data['daily']['generated_energy_kwh'].append(round(generated_energy_kwh,3))

            return JsonResponse(data)
        else:
            return HttpResponseBadRequest(json.dumps(serializer.errors), content_type="application/json")
    
