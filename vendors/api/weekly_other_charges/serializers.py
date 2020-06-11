from rest_framework import serializers
from .models import WeeklyOtherCharges


class WeeklyOtherChargesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyOtherCharges
        fields = '__all__'