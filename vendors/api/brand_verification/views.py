from rest_framework import viewsets
from .serializers import VendorDocumentAuthSerializer,ListVendorDocumentAuthSerializer
from .models import VendorDocumentAuth
from rest_framework.response import Response
import requests


class VendorDocumentAuthViewSet(viewsets.ModelViewSet):
    queryset = VendorDocumentAuth.objects.all()
    serializer_class = VendorDocumentAuthSerializer


class VendorDocumentAuthListViewSet(viewsets.ViewSet):
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
        for i in range(len(brand_verification)):
            item = {
                    'brand_verification_id':brand_verification[i]['id'],
                    'agreement_id' : brand_verification[i]['agreement_id'],
                    'type' :brand_verification[i]['type'],
                    'file' :brand_verification[i]['file'],
                    'start_date' :brand_verification[i]['start_date'],
                    'expiry_date' :brand_verification[i]['expiry_date'],
                    'updated_at' :brand_verification[i]['updated_at'],
                    'is_notification_delivered' :brand_verification[i][ 'is_notification_delivered'],
                    'ip_address' :brand_verification[i]['ip_address'],
                    }
            vendors_response = dict(
                requests.get('http://13.232.166.20/vendors/' + str(brand_verification[i]['id']) + '/', headers={'authorization': token}).json())
            item['brand_id'] = vendors_response['brand_id']
            item['vendor_id'] = vendors_response['vendor_id']
            data.append(item)
        if len(data):
            serializer =ListVendorDocumentAuthSerializer(data, many=True)
            new_data=serializer.data
            for obj in serializer.data:
                if len(columns)>0:
                    columns.append('id')
                    columns.append('brand_id')
                    columns.append('vendor_id')
                    new_data= {key: value for (key, value) in obj.items() if key in columns}
            return Response({'header': header, 'selected_headers': selected_headers, 'data': new_data, 'message': 'brand_verification fetched successfully'})
        else:
            data = []
            return Response({'header': header,'selected_headers': selected_headers, 'data': data, 'message': 'No brand_verification found'})