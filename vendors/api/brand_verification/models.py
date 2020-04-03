from django.db import models


class VendorDocumentAuth(models.Model):
    agreement_id = models.CharField(max_length=30, blank=True, null=True)
    brand_id = models.IntegerField(blank=True, null=True)
    vendor_id = models.IntegerField()
    type = models.CharField(max_length=30)
    file = models.FileField(upload_to='uploads/vendor_docs/')
    start_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    is_notification_delivered = models.BooleanField()
    ip_address = models.CharField(max_length=35, blank=True, null=True)
