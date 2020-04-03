from django.db import models


class Brand(models.Model):
    brand_name = models.CharField(max_length=255)
    vendor_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
