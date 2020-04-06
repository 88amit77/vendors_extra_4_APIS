from rest_framework import viewsets
from .serializers import MobileTicketSerializer,ListMobileTicketSerializer
from .models import MobileTicket
from rest_framework.response import Response
import requests


class MobileTicketDetailsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = MobileTicket.objects.all()
    serializer_class = MobileTicketSerializer

class MobileTicketListViewSet(viewsets.ViewSet):
    def list(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        mobile_ticket = requests.get('http://localhost:8001/mobile_ticket/').json()
        data = []
        for i in range(len(mobile_ticket)):
            item = {
                    'mobile_ticket_id':mobile_ticket[i]['id'],
                    'brand_coordinator': mobile_ticket[i]['brand_coordinator'],
                    'title':mobile_ticket[i]['title'],
                    'department_name':mobile_ticket[i]['department_name'],
                    'status':mobile_ticket[i]['status'],
                    'created_by':mobile_ticket[i]['created_by'],
                    'created_at':mobile_ticket[i]['created_at'],
                    'upload_at':mobile_ticket[i]['upload_at'],
                    'due_date':mobile_ticket[i]['due_date']
                    }
            vendors_response = dict(
                requests.get('http://13.232.166.20/vendors/' + str(mobile_ticket[i]['id']) + '/', headers={'authorization': token}).json())
            item['vendor_name'] = vendors_response['vendor_name']
            data.append(item)
        if len(data):
            serializer = ListMobileTicketSerializer(data, many=True)
            return Response(serializer.data)
        else:
            data = []
            return Response(data)

