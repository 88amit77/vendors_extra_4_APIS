from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ListVendorSerializer, NewVendorDetailsSerializer
from .models import NewVendorDetails
from rest_framework.response import Response
import requests

class VendorListViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def list(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        auth_user = requests.get('http://13.232.166.20/auth/users/me/', headers={'authorization': token}).json()
        # return Response({'auth_user': auth_user})
        permissions = []
        for i in range(len(auth_user['user_permissions'])):
            permissions.append(auth_user['user_permissions'][i]['codename'])
        for i in range(len(auth_user['groups'])):
            for j in range(len(auth_user['groups'][i]['permissions'])):
                permissions.append(auth_user['groups'][i]['permissions'][j]['codename'])
        permissions = set(permissions)
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
            user_response = dict(requests.get('http://13.232.166.20/users/1/', headers={'authorization': 'Bearer '+token}).json())
            item['user_name'] = user_response['username']
            item['email'] = user_response['email']
            marketing_incharge_response = dict(requests.get('http://13.232.166.20/users/2/', headers={'authorization': 'Bearer '+token}).json())
            brand_analyst_response = dict(requests.get('http://13.232.166.20/users/3/', headers={'authorization': 'Bearer '+token}).json())
            item['marketing_incharge_name'] = marketing_incharge_response['username']
            item['brand_analyst_name'] = brand_analyst_response['username']
            data.append(item)
            return Response(data)


class NewVendorDetailsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = NewVendorDetails.objects.all()
    serializer_class = NewVendorDetailsSerializer
