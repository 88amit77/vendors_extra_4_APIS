from django.db import models

class MobileTicket(models.Model):
    '''   model for mobile_ticket '''
    ticket_id=models.IntegerField()
    brand_coordinator_id=models.IntegerField()
    vendor_name=models.CharField(max_length=30)
    title=models.CharField(max_length=50)
    department_name=models.CharField(max_length=20)
    status=models.BinaryField()
    created_by=models.CharField(max_length=25)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title

    #dependent
    #vendor_name
class  MobileTicketReply(models.Model):
    message=models.CharField(max_length=100)
    send_by=models.CharField(max_length=20)
    file_path=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    ticket_id=models.CharField(max_length=100)

    #dependent on mobile ticket
    # Ticket_id

