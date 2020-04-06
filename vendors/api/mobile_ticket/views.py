from rest_framework import viewsets
from .serializers import MobileTicketSerializer,ListMobileTicketSerializer,MobileTicketReplySerializer,ListMobileTicketReplySerializer
from .models import MobileTicket,MobileTicketReply
from rest_framework.response import Response
import requests


class MobileTicketDetailsViewSet(viewsets.ModelViewSet):

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

class MobileTicketReplyViewSet(viewsets.ModelViewSet):

    queryset = MobileTicketReply.objects.all()
    serializer_class = MobileTicketReplySerializer

class MobileTicketReplyListViewSet(viewsets.ViewSet):
    def list(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        mobile_ticket_reply = requests.get('http://localhost:8001/mobile_ticket_reply/').json()
        data = []
        for i in range(len(mobile_ticket_reply)):
            item = {
                   'mobile_ticket_reply_id': mobile_ticket_reply[i]['id'],
                   'message' : mobile_ticket_reply[i]['message'],
                   'send_by' : mobile_ticket_reply[i]['send_by'],
                   'file_path': mobile_ticket_reply[i]['file_path'],
                   'created_at': mobile_ticket_reply[i][ 'created_at'],
                   'updated_at' : mobile_ticket_reply[i]['updated_at'],


                    }
            mobile_ticket_response = dict(
                requests.get('http://13.232.166.20/mobile_ticket/' + str(mobile_ticket_reply[i]['id']) + '/', headers={'authorization': token}).json())
            item['mobile_ticket_id'] = mobile_ticket_response['id']
            data.append(item)
        if len(data):
            serializer = ListMobileTicketReplySerializer(data, many=True)
            return Response(serializer.data)
        else:
            data = []
            return Response(data)