from rest_framework import viewsets
from .serializers import VendorDocumentAuthSerializer,ListVendorDocumentAuthSerializer
from .models import VendorDocumentAuth
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
import requests

class VendorDocumentAuthViewSetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit =3
class VendorDocumentAuthViewSet(viewsets.ModelViewSet):
    queryset = VendorDocumentAuth.objects.all()
    serializer_class = VendorDocumentAuthSerializer
    pagination_class =VendorDocumentAuthViewSetPagination

class VendorDocumentAuthListViewSet(viewsets.ViewSet):
    pagination_class = PageNumberPagination
    def list(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if 'columns' in request.data:
            columns = request.data['columns'].split(',')
            selected_headers = {i: columns[i] for i in range(0, len(columns))}
        else:
            columns = []
            selected_headers = {}
        brand_verification = requests.get('http://localhost:8001/brand_verification/').json()
        data = []
        header = {

            'agreement_id': 'agreement_id',
            'type': 'type',
            'file': 'file',
            'start_date':'start_date',
            'expiry_date':'expiry_date',
            'updated_at': 'updated_at',
            'is_notification_delivered': 'is_notification_delivered',
            'ip_address': 'ip_address',
            'brand_id': 'brand_id',
            'vendor_id':'vendor_id'
           }
        brand_verification_data = brand_verification['results']
        for i in range(len(brand_verification_data)):
            item = {
                    'brand_verification_id':brand_verification_data[i]['id'],
                    'agreement_id' : brand_verification_data[i]['agreement_id'],
                    'type' :brand_verification_data[i]['type'],
                    'file' :brand_verification_data[i]['file'],
                    'start_date' :brand_verification_data[i]['start_date'],
                    'expiry_date' :brand_verification_data[i]['expiry_date'],
                    'updated_at' :brand_verification_data[i]['updated_at'],
                    'is_notification_delivered' :brand_verification_data[i][ 'is_notification_delivered'],
                    'ip_address' :brand_verification_data[i]['ip_address'],
                    }
            vendors_response = dict(
                requests.get('http://13.232.166.20/vendors/' + str(brand_verification_data[i]['id']) + '/', headers={'authorization': token}).json())
            item['brand_id'] = vendors_response['brand_id']
            item['vendor_id'] = vendors_response['vendor_id']
            data.append(item)
        new_data = []
        if len(data):
            serializer =ListVendorDocumentAuthSerializer(data, many=True)
            if len(columns) > 0:
                for obj in serializer.data:
                    columns.append('id')
                    columns.append('brand_id')
                    columns.append('vendor_id')
                    new_item = {key: value for (key, value) in obj.items() if key in columns}
                    new_data.append(new_item)
                else:
                    new_data = serializer.data
                return Response({'count': brand_verification['count'], 'next': brand_verification['next'], 'previous': brand_verification['previous'],
                                 'header': header, 'selected_headers': selected_headers, 'data': new_data,
                                 'message': 'brand_verification fetched successfully'})
        else:
            data = []
            return Response(
                {'count': 0, 'next': None, 'previous': None, 'header': header, 'selected_headers': selected_headers,
                 'data': data, 'message': 'No brand_verification found'})