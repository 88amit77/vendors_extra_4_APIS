from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from .list_vendors.views import VendorListViewSet, NewVendorDetailsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'vendors', NewVendorDetailsViewSet, basename='vendors')
router.register(r'list_vendors', VendorListViewSet, basename='vendors_list')
# TODO: add here your API URLs

schema_view = get_swagger_view(title='Micromerce API')

urlpatterns = [
	path('', include(router.urls)),
	path("vendors/docs/", schema_view),
]

