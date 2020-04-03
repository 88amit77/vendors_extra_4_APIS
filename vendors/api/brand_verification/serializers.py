from rest_framework import serializers
from .models import VendorDocumentAuth


class VendorDocumentAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorDocumentAuth
        fields = '__all__'

