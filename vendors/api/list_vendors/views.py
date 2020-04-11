from rest_framework import viewsets
from .serializers import ListVendorSerializer, NewVendorDetailsSerializer
from .models import NewVendorDetails
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
import requests


class VendorListViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    pagination_class = PageNumberPagination

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
        if 'columns' in request.data:
            columns = request.data['columns'].split(',')
            selected_headers = {i: columns[i] for i in range(0, len(columns))}
        else:
            columns = []
            selected_headers = {}

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
        vendor_data = vendors['results']
        for i in range(len(vendor_data)):
            item = {'user_id': vendor_data[i]['user_id'], 'vendor_id': vendor_data[i]['id'],
                    'vendor_name': vendor_data[i]['vendor_name'], 'phone': vendor_data[i]['mobile'], 'vendor_code': '000',
                    'vendor_type': vendor_data[i]['vendor_type'], 'current_status': 'New', 'currency': 'INR'}

            user_response = dict(
                requests.get('http://13.232.166.20/users/' + str(vendor_data[i]['user_id']) + '/', headers={'authorization': token}).json())
            item['user_name'] = user_response['username']
            item['email'] = user_response['email']
            marketing_incharge_response = dict(
                requests.get('http://13.232.166.20/users/' + str(vendor_data[i]['marketing_incharge_id']) + '/', headers={'authorization': token}).json())
            brand_analyst_response = dict(
                requests.get('http://13.232.166.20/users/' + str(vendor_data[i]['brand_coordinators_id']) + '/', headers={'authorization': token}).json())
            item['marketing_incharge_name'] = marketing_incharge_response['username']
            item['brand_coordinators_name'] = brand_analyst_response['username']
            data.append(item)
        new_data = []
        if len(data):
            serializer = ListVendorSerializer(data, many=True)
            if len(columns) > 0:
                for obj in serializer.data:
                    columns.append('user_id')
                    columns.append('user_name')
                    new_item = {key: value for (key, value) in obj.items() if key in columns}
                    new_data.append(new_item)
            else:
                new_data = serializer.data
            return Response({'count': vendors['count'], 'next': vendors['next'], 'previous': vendors['previous'],
                             'header': header, 'selected_headers': selected_headers, 'data': new_data,
                             'message': 'Vendors fetched successfully'})
        else:
            data = []
            return Response({'count': 0, 'next': None, 'previous': None, 'header': header, 'selected_headers': selected_headers, 'data': data, 'message': 'No vendor found'})

class NewVendorDetailsViewSetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit =3
class NewVendorDetailsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = NewVendorDetails.objects.all()
    serializer_class = NewVendorDetailsSerializer
    pagination_class =NewVendorDetailsViewSetPagination