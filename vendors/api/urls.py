from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from .brand_verification.views import VendorDocumentAuthViewSet,VendorDocumentAuthListViewSet
from .list_vendors.views import VendorListViewSet, NewVendorDetailsViewSet
from .brands.views import BrandViewSet
from .mobile_ticket.views import MobileTicketListViewSet,MobileTicketDetailsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'vendors', NewVendorDetailsViewSet, basename='vendors')
router.register(r'list_vendors', VendorListViewSet, basename='vendors_list')
router.register(r'brand_verification', VendorDocumentAuthViewSet, basename='brand_verification')
router.register(r'List_brand_verification', VendorDocumentAuthListViewSet, basename='List_brand_verification')
router.register(r'brands', BrandViewSet, basename='brands')
router.register(r'mobile_ticket', MobileTicketDetailsViewSet, basename='mobile_ticket')
router.register(r'list_mobile_ticket', MobileTicketListViewSet, basename='list_mobile_ticket')
# TODO: add here your API URLs

schema_view = get_swagger_view(title='Micromerce API')

urlpatterns = [
	path('', include(router.urls)),
	path("vendors/docs/", schema_view),
]

