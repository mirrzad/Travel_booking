from rest_framework import serializers
from django.utils import timezone
from bookings.models import Trip


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
        extra_kwargs = {
            'destination': {'required': True},
            'departure_date': {'required': True},
            'return_date': {'required': True},
        }

    def validate(self, attrs):
        if attrs['departure_date'] < timezone.now().date() or attrs['return_date'] < attrs['departure_date']:
            raise serializers.ValidationError('Enter a valid date.')
        return super().validate(attrs)
