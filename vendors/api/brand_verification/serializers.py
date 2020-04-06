from rest_framework import serializers
from .models import VendorDocumentAuth


class VendorDocumentAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorDocumentAuth
        fields = '__all__'


class ListVendorDocumentAuthSerializer(serializers.Serializer):
    agreement_id = serializers.CharField(max_length=30, blank=True, null=True)
    brand_id =serializers.IntegerField(blank=True, null=True)
    vendor_id = serializers.IntegerField()
    type = serializers.CharField(max_length=30)
    file = serializers.FileField(upload_to='uploads/vendor_docs/')
    start_date =serializers.DateTimeField(auto_now_add=True)
    expiry_date =serializers.DateTimeField()
    updated_at =serializers.DateTimeField(auto_now=True)
    is_notification_delivered =serializers.BooleanField()
    ip_address =serializers.CharField(max_length=35, blank=True, null=True)




