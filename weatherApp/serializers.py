from rest_framework import serializers

class WeatherParametersSerializer(serializers.Serializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()

    def validate_latitude(self, value):
        if not isinstance(value, (int, float)):
            raise serializers.ValidationError("Latitude must be a numeric value.")
        if value < -90 or value > 90:
            raise serializers.ValidationError("Latitude must be within range -90 to 90 degrees.")
        return value

    def validate_longitude(self, value):
        if not isinstance(value, (int, float)):
            raise serializers.ValidationError("Longitude must be a numeric value.")
        if value < -180 or value > 180:
            raise serializers.ValidationError("Longitude must be within range -180 to 180 degrees.")
        return value
