from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from .brand_verification.views import VendorDocumentAuthViewSet
from .list_vendors.views import VendorListViewSet, NewVendorDetailsViewSet
from .brands.views import BrandViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'vendors', NewVendorDetailsViewSet, basename='vendors')
router.register(r'list_vendors', VendorListViewSet, basename='vendors_list')
router.register(r'vendors_document_auth', VendorDocumentAuthViewSet, basename='vendors_document_auth')
router.register(r'brands', BrandViewSet, basename='brands')
# TODO: add here your API URLs

schema_view = get_swagger_view(title='Micromerce API')

urlpatterns = [
	path('', include(router.urls)),
	path("vendors/docs/", schema_view),
]

