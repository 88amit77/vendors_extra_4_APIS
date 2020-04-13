from rest_framework import viewsets
from .serializers import BrandSerializer
from .models import Brand
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
import requests
from rest_framework import filters

class BrandViewSetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit =3

class BrandViewSet(viewsets.ModelViewSet):
    search_fields = ['brand_name', 'vendor_id', 'created_at', 'updated_at']
    ordering_fields = ['created_at', 'updated_at']
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    pagination_class = BrandViewSetPagination
