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
        brand_verification = requests.get('http://localhost:8001/brand_verification/').json()
        data = []
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
            return Response(serializer.data)
        else:
            data = []
            return Response(data)