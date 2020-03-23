from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ListVendorSerializer
from .models import NewVendorDetails
from rest_framework.response import Response
import requests

class VendorListViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def list(self, request):
        vendors = NewVendorDetails.objects.all()
        data = []
        for i in range(len(vendors)):
            item = {
                'user_id': i + 1,
                'user_name': 'Abc',
                'email': 'abc@gmail.com',
                'vendor_name': vendors[i]['vendor_name'],
                'phone': vendors['mobile'],
                'vendor_code': 'xxx',
                'vendor_type': vendors['vendor_type'],
                'current_status': 'New',
                'currency': 'INR',
                'marketing_incharge_name': 'ABC',
                'brand_analyst_name': 'ABC'
            }
            data.append(item)
        if len(data):
            serializer = ListVendorSerializer(data)
            return Response(serializer.data)
        else:
            item = {
                'user_id': 1,
                'vendor_name': 'test',
                'phone': '9987655679',
                'vendor_code': 'xxx',
                'vendor_type': 'new',
                'current_status': 'New',
                'currency': 'INR',
                'marketing_incharge_name': 'ABC',
                'brand_analyst_name': 'ABC'
            }
            token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg0OTY3MDU5LCJqdGkiOiIzMGQwYTBiYjI3ZWM0YTgwODdkZWZmYWNlNmQ0ZDAyYyIsInVzZXJfaWQiOjF9.fTmnu_ub2Cj7ZevpCWMPCYiax8iH7587mlWeaZuvLaQ'
            user_response = dict(requests.get('http://172.17.0.1:8002/users/1/', headers={'authorization': 'Bearer '+token}).json())
            item['user_name'] = user_response['username']
            item['email'] = user_response['email']
            marketing_incharge_response = dict(requests.get('http://172.17.0.1:8002/users/2/', headers={'authorization': 'Bearer '+token}).json())
            brand_analyst_response = dict(requests.get('http://172.17.0.1:8002/users/3/', headers={'authorization': 'Bearer '+token}).json())
            item['marketing_incharge_name'] = marketing_incharge_response['username']
            item['brand_analyst_name'] = brand_analyst_response['username']
            data.append(item)
            return Response(data)
