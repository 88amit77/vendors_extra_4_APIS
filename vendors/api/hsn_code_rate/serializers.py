from rest_framework import serializers
from .models import HsnCodeRate


class HsnCodeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HsnCodeRate
        fields = '__all__'