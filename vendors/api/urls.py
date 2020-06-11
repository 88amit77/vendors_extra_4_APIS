from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from .purchase_sku_detail.views import PurchaseSkuDetailsViewSet
from .purchase_invoices.views import PurchaseInvoicesViewSet
from .weekly_other_charges.views import WeeklyOtherChargesViewSet
from .hsn_code_rate.views import HsnCodeRateViewSet



from rest_framework.routers import DefaultRouter

router = DefaultRouter()


schema_view = get_schema_view(openapi.Info(
      title="Vendors API",
      default_version='v1',
      description="Test description",
   ), public=True, permission_classes=(permissions.AllowAny,))
# new added APIs
router.register(r'hsn_code_rate', HsnCodeRateViewSet, basename='hsn_code_rate')
router.register(r'purchase_invoices', PurchaseInvoicesViewSet, basename='purchase_invoices')
router.register(r'purchase_sku_detail', PurchaseSkuDetailsViewSet, basename='purchase_sku_detail')
router.register(r'weekly_other_charges', WeeklyOtherChargesViewSet, basename='weekly_other_charges')

urlpatterns = [
    path('', include(router.urls)),
    path("docs/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]