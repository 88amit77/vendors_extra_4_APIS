from rest_framework import viewsets
from .serializers import VendorDocumentAuthSerializer
from .models import VendorDocumentAuth
from rest_framework.response import Response
import requests


class VendorDocumentAuthViewSet(viewsets.ModelViewSet):
    queryset = VendorDocumentAuth.objects.all()
    serializer_class = VendorDocumentAuthSerializer
