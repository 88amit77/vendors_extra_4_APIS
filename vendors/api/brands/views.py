from rest_framework import viewsets
from .serializers import BrandSerializer
from .models import Brand
from rest_framework.response import Response
import requests


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
