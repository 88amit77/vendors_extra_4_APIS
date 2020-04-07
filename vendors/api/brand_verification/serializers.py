from rest_framework import serializers
from .models import VendorDocumentAuth


class VendorDocumentAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorDocumentAuth
        fields = '__all__'


class ListVendorDocumentAuthSerializer(serializers.Serializer):
    agreement_id = serializers.CharField(max_length=30, allowNone=True)
    brand_id =serializers.IntegerField(allowNone=True)
    vendor_id = serializers.IntegerField()
    type = serializers.CharField(max_length=30)
    file = serializers.FileField()
    start_date =serializers.DateTimeField()
    expiry_date =serializers.DateTimeField()
    updated_at =serializers.DateTimeField()
    is_notification_delivered =serializers.BooleanField()
    ip_address =serializers.CharField(max_length=35, allowNone=True)
