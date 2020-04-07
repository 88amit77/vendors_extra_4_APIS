from rest_framework import serializers
from .models import (MobileTicket)




class MobileTicketSerializer(serializers.ModelSerializer):

    class Meta:
         model=MobileTicket
         fields='__all__'

class ListMobileTicketSerializer(serializers.Serializer):
    brand_coordinator = serializers.CharField(max_length=25)
    vendor_name=serializers.CharField(max_length=30)
    title = serializers.CharField(max_length=50)
    department_name = serializers.CharField(max_length=20)
    status = serializers.IntegerField()
    created_by = serializers.CharField(max_length=25)
    created_at = serializers.DateTimeField()
    upload_at = serializers.DateTimeField()
    due_date = serializers.DateTimeField()

