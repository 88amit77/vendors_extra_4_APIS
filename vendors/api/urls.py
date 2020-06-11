from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from .brand_verification.views import VendorDocumentAuthViewSet,VendorDocumentAuthListViewSet
from .list_vendors.views import (
	VendorListViewSet,
	NewVendorDetailsViewSet,
	UserIdFilterView,
	UsernameFilterView,
	MarketingInchargeFilterView,
	BrandCoordinatorsFilterView,
	EmailFilterView,
	VendorNameFilterView,
)
from .brands.views import BrandViewSet
from .mobile_ticket.views import (
	MobileTicketListViewSet,
	MobileTicketDetailsViewSet,
	MobileTicketReplyViewSet,
	MobileTicketReplyListViewSet
)
from .hsn_code_rate.views import HsnCodeRateViewSet
from .purchase_invoices.views import PurchaseInvoicesViewSet
from .purchase_sku_detail.views import PurchaseSkuDetailsViewSet
from .weekly_other_charges.views import WeeklyOtherChargesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'vendors', NewVendorDetailsViewSet, basename='vendors')
router.register(r'list_vendors', VendorListViewSet, basename='vendors_list')
router.register(r'brand_verification', VendorDocumentAuthViewSet, basename='brand_verification')
router.register(r'List_brand_verification', VendorDocumentAuthListViewSet, basename='List_brand_verification')
router.register(r'brands', BrandViewSet, basename='brands')
router.register(r'mobile_ticket', MobileTicketDetailsViewSet, basename='mobile_ticket')
router.register(r'list_mobile_ticket', MobileTicketListViewSet, basename='list_mobile_ticket')
router.register(r'mobile_ticket_reply', MobileTicketReplyViewSet, basename='mobile_ticket_reply')
router.register(r'list_mobile_ticket_reply', MobileTicketReplyListViewSet, basename='list_mobile_ticket_reply')
#new added APIs
router.register(r'hsn_code_rate', HsnCodeRateViewSet, basename='hsn_code_rate')
router.register(r'purchase_invoices', PurchaseInvoicesViewSet, basename='purchase_invoices')
router.register(r'purchase_sku_detail', PurchaseSkuDetailsViewSet, basename='purchase_sku_detail')
router.register(r'weekly_other_charges', WeeklyOtherChargesViewSet, basename='weekly_other_charges')



schema_view = get_swagger_view(title='Micromerce API')

urlpatterns = [
	path('', include(router.urls)),
	path('user_id/', UserIdFilterView.as_view(), name='userid_filter'),
	path('user_name/', UsernameFilterView.as_view(), name='username_filter'),
	path('email/', EmailFilterView.as_view(), name='email_filter'),
	path('marketing_incharge_name/', MarketingInchargeFilterView.as_view(), name='marketing_incharge_filter'),
	path('brand_coordinators_name/', BrandCoordinatorsFilterView.as_view(), name='brand_analyst_filter'),
	path('vendor_name/', VendorNameFilterView.as_view(), name='vendor_name'),
	path("vendors/docs/", schema_view),
]

