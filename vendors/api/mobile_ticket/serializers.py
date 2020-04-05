from rest_framework import serializers
from .models import (MobileTicket)




class MobileTicketSerializer(serializers.ModelSerializer):

    class Meta:
         model=MobileTicket
         fields='__all__'