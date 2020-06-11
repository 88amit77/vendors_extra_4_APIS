from rest_framework import serializers
from .models import PurchaseSkuDetails


class PurchaseSkuDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseSkuDetails
        fields = '__all__'