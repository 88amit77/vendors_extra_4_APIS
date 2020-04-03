from rest_framework import serializers
from .models import NewVendorDetails


class ListVendorSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    user_name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    vendor_name = serializers.CharField(max_length=200)
    phone = serializers.CharField(max_length=200)
    vendor_code = serializers.CharField(max_length=200)
    vendor_type = serializers.CharField(max_length=200)
    current_status = serializers.CharField(max_length=200)
    currency = serializers.CharField(max_length=200)
    marketing_incharge_name = serializers.CharField(max_length=200)
    brand_analyst_name = serializers.CharField(max_length=200)


class NewVendorDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewVendorDetails
        fields = '__all__'