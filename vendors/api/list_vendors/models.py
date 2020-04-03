from django.db import models


# Create your models here.
class NewVendorDetails(models.Model):
    brand_id = models.IntegerField()
    user_id = models.IntegerField()
    vendor_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    pincode = models.CharField(max_length=10)
    mobile = models.CharField(max_length=15)
    optional_phone = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(max_length=20)
    marketing_incharge_id=models.IntegerField()
    brand_coordinators_id=models.IntegerField()
    pan = models.CharField(max_length=20)
    gst_input = models.CharField(max_length=20)
    portal_accepted_for_listing = models.IntegerField()
    no_multi_portal_fee = models.FloatField()
    insurance = models.CharField(max_length=30)
    no_storage_fee = models.FloatField()
    fair_participation = models.CharField(max_length=20)
    amazon = models.BooleanField()
    flipkart = models.BooleanField()
    paytm = models.BooleanField()
    snapdeal = models.BooleanField()
    tatacliq = models.BooleanField()
    myntra = models.BooleanField()
    vendor_type = models.CharField(max_length=10)
    state_pan = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=20)
    ifsc_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vendor_name
