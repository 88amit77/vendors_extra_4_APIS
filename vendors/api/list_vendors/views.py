import json
from rest_framework import viewsets
from .serializers import ListVendorSerializer, NewVendorDetailsSerializer
from .models import NewVendorDetails
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from rest_framework.views import APIView
import requests


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'


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

        if 'columns' in request.data:
            columns = request.data['columns'].split(',')
            selected_headers = {i: columns[i] for i in range(0, len(columns))}
        else:
            columns = []
            selected_headers = {}

        if 'page' in request.query_params:
            page = request.query_params['page']
        else:
            page = 1
        if 'page_size' in request.query_params:
            page_size = request.query_params['page_size']
        else:
            page_size = 20
        vendors = requests.get('http://localhost:8001/vendors/?page=' + str(page) + '&page_size='+str(page_size)).json()

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
            'marketing_incharge_name': 'Marketing Incharge Name',
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
            next_link = None
            prev_link = None
            if vendors['next'] is not None:
                next_link = '/list_vendors/?' + vendors['next'].split('?')[1]
            if vendors['previous'] is not None:
                prev_link = '/list_vendors/?' + vendors['previous'].split('?')[1]
            return Response({'count': vendors['count'], 'next': next_link, 'previous': prev_link,
                             'header': header, 'selected_headers': selected_headers, 'data': new_data,
                             'message': 'Vendors fetched successfully'})
        else:
            data = []
            return Response({'count': 0, 'next': None, 'previous': None, 'header': header, 'selected_headers': selected_headers, 'data': data, 'message': 'No vendor found'})


class NewVendorDetailsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = NewVendorDetails.objects.order_by('-id')
    serializer_class = NewVendorDetailsSerializer
    pagination_class = CustomPageNumberPagination


class UserIdFilterView(APIView):
    def get(self, request, *args,**kwargs):
        qs = NewVendorDetails.objects.all()
        ids = [str(data.user_id) for data in qs]
        id = ",".join(ids)
        data = {'id': id}
        if 'user_id' in request.data:
            data['user_id'] = request.data['user_id']
        user_ids = requests.get('http://13.232.166.20/userid_filter/', data=data).json()
        return Response(user_ids)


class UsernameFilterView(APIView):
    def get(self, request, *args,**kwargs):
        qs = NewVendorDetails.objects.all()
        ids = [str(data.user_id) for data in qs]
        id = ",".join(ids)
        data = {'id': id}
        if 'user_name' in request.data:
            data['username'] = request.data['user_name']
        user_ids = requests.get('http://13.232.166.20/username_filter/', data=data).json()
        return Response(user_ids)


class EmailFilterView(APIView):
    def get(self, request, *args,**kwargs):
        qs = NewVendorDetails.objects.all()
        ids = [str(data.user_id) for data in qs]
        id = ",".join(ids)
        data = {'id': id}
        if 'email' in request.data:
            data['email'] = request.data['email']
        user_ids = requests.get('http://13.232.166.20/email_filter/', data=data).json()
        return Response(user_ids)


class MarketingInchargeFilterView(APIView):
    def get(self, request, *args,**kwargs):
        qs = NewVendorDetails.objects.all()
        ids = [str(data.marketing_incharge_id) for data in qs]
        id = ",".join(ids)
        data = {'id': id}
        if 'marketing_incharge_name' in request.data:
            data['username'] = request.data['marketing_incharge_name']
        user_ids = requests.get('http://13.232.166.20/username_filter/', data=data).json()
        return Response(user_ids)


class BrandCoordinatorsFilterView(APIView):
    def get(self, request, *args,**kwargs):
        qs = NewVendorDetails.objects.all()
        ids = [str(data.brand_coordinators_id) for data in qs]
        id = ",".join(ids)
        data = {'id': id}
        if 'brand_coordinators_name' in request.data:
            data['username'] = request.data['brand_coordinators_name']
        user_ids = requests.get('http://13.232.166.20/username_filter/', data=data).json()
        return Response(user_ids)


class VendorNameFilterView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        qs = NewVendorDetails.objects.distinct('vendor_name')
        if 'vendor_name' in request.data:
            qs = qs.filter(vendor_name__contains=request.data['vendor_name'])
        vendors = [{vendor.vendor_name: vendor.vendor_name} for vendor in qs]
        return Response(vendors)