from django.db import models

class MobileTicket(models.Model):
    '''   model for mobile_ticket '''
    brand_coordinator=models.CharField(max_length=25)
    #vendor_name=models.CharField(max_length=30)
    title=models.CharField(max_length=50)
    department_name=models.CharField(max_length=20)
    status=models.BinaryField()
    created_by=models.CharField(max_length=25)
    created_at=models.DateTimeField()
    upload_at=models.DateTimeField()
    due_date=models.DateTimeField()


    def __str__(self):
        return self.title

    #dependent
    #vendor_name
