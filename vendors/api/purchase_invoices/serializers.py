from rest_framework import serializers
from .models import PurchaseInvoices


class PurchaseInvoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseInvoices
        fields = '__all__'