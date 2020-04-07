from rest_framework import viewsets
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
        vendors = requests.get('http://localhost:8001/vendors/').json()
        data = []
        header = {
            'user_id': 'User Id',
            'user_name': 'Username',
            'email': 'Email',
            'vendor_name': 'Vendor Name',
            'phone': 'Phone',
            'vendor_code': 'Vendor Code',
            'vendor_type': 'Vendor type',
            'current_status': 'Current Status',
            'currency': 'Currency',
            'marketing_incharge_name': 'Markettig Incharge Name',
            'brand_coordinators_name': 'Brand Coordinator Name'
        }
        for i in range(len(vendors)):
            item = {
                'vendor_id': vendors[i]['id'],
                'user_id': vendors[i]['user_id'],
                'vendor_name': vendors[i]['vendor_name'],
                'phone': vendors[i]['mobile'],
                'vendor_code': '000',
                'vendor_type': vendors[i]['vendor_type'],
                'current_status': 'New',
                'currency': 'INR'
            }
            user_response = dict(
                requests.get('http://13.232.166.20/users/' + str(vendors[i]['user_id']) + '/', headers={'authorization': token}).json())
            item['user_name'] = user_response['username']
            item['email'] = user_response['email']
            marketing_incharge_response = dict(
                requests.get('http://13.232.166.20/users/' + str(vendors[i]['marketing_incharge_id']) + '/', headers={'authorization': token}).json())
            brand_analyst_response = dict(
                requests.get('http://13.232.166.20/users/' + str(vendors[i]['brand_coordinators_id']) + '/', headers={'authorization': token}).json())
            item['marketing_incharge_name'] = marketing_incharge_response['username']
            item['brand_coordinators_name'] = brand_analyst_response['username']
            data.append(item)
        if len(data):
            serializer = ListVendorSerializer(data, many=True)
            return Response({'header': header, 'data': serializer.data, 'message': 'Vendors fetched successfully'})
        else:
            data = []
            return Response({'header': header, 'data': data, 'message': 'No vendor found'})


class NewVendorDetailsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = NewVendorDetails.objects.all()
    serializer_class = NewVendorDetailsSerializer
