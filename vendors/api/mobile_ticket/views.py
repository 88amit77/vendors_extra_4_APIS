from rest_framework import viewsets
from .serializers import MobileTicketSerializer,ListMobileTicketSerializer,MobileTicketReplySerializer,ListMobileTicketReplySerializer
from .models import MobileTicket,MobileTicketReply
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
import requests
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class MobileTicketDetailsViewSetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit =3

class MobileTicketDetailsViewSet(viewsets.ModelViewSet):
    search_fields = ['ticket_id', 'brand_coordinator_id', 'vendor_name', 'title','department_name','status','created_by','created_at','updated_at','due_date']
    ordering_fields = ['created_at','updated_at','due_date']
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    queryset = MobileTicket.objects.all()
    serializer_class = MobileTicketSerializer
    pagination_class = MobileTicketDetailsViewSetPagination

class MobileTicketListViewSet(viewsets.ViewSet):
    pagination_class = PageNumberPagination
    def list(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if 'columns' in request.data:
            columns = request.data['columns'].split(',')
            selected_headers = {i: columns[i] for i in range(0, len(columns))}
        else:
            columns = []
            selected_headers = {}
        mobile_ticket = requests.get('http://localhost:8001/mobile_ticket/').json()
        data = []
        header = {
            'ticket_id':'mobile_ticket_id',
            'brand_coordinator_id': 'brand_coordinator_id',
            'vendor_name': 'vendor_name',
            'title':'title',
            'department_name':'department_name',
            'status':'status',
            'created_by':'created_by',
            'created_at':'created_at',
            'updated_at': 'updated_at',
            'due_date': 'due_date',

            }
        mobile_ticket_data = mobile_ticket['results']
        for i in range(len(mobile_ticket)):
            item = {
                    'mobile_ticket_id':mobile_ticket_data[i]['id'],
                    'brand_coordinator_id': mobile_ticket_data[i]['brand_coordinator_id'],
                    'title':mobile_ticket_data[i]['title'],
                    'department_name':mobile_ticket_data[i]['department_name'],
                    'status':mobile_ticket_data[i]['status'],
                    'created_by':mobile_ticket_data[i]['created_by'],
                    'created_at':mobile_ticket_data[i]['created_at'],
                    'updated_at':mobile_ticket_data[i]['updated_at'],
                    'due_date': mobile_ticket_data[i]['due_date'],

                    }
            vendors_response = dict(
                requests.get('http://13.232.166.20/vendors/' + str(mobile_ticket_data[i]['id']) + '/', headers={'authorization': token}).json())
            item['vendor_name'] = vendors_response['vendor_name']
            data.append(item)
        new_data = []
        if len(data):
            serializer =ListMobileTicketSerializer(data, many=True)
            if len(columns) > 0:
                for obj in serializer.data:
                    columns.append('id')
                    columns.append('vendor_name')
                    new_item = {key: value for (key, value) in obj.items() if key in columns}
                    new_data.append(new_item)
                else:
                    new_data = serializer.data
                return Response({'count': mobile_ticket['count'], 'next': mobile_ticket['next'],
                                 'previous': mobile_ticket['previous'],
                                 'header': header, 'selected_headers': selected_headers, 'data': new_data,
                                 'message': 'mobile_ticket fetched successfully'})
        else:
            data = []
            return Response(
                {'count': 0, 'next': None, 'previous': None, 'header': header, 'selected_headers': selected_headers,
                 'data': data, 'message': 'No mobile_ticket found'})

class MobileTicketReplyViewSetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit =3


class MobileTicketReplyViewSet(viewsets.ModelViewSet):
    search_fields = ['message', 'send_by', 'file_path', 'created_at', 'updated_at', 'ticket_id']
    ordering_fields = ['created_at', 'updated_at']
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    queryset = MobileTicketReply.objects.all()
    serializer_class = MobileTicketReplySerializer
    pagination_class = MobileTicketReplyViewSetPagination

class MobileTicketReplyListViewSet(viewsets.ViewSet):
    pagination_class = PageNumberPagination
    def list(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if 'columns' in request.data:
            columns = request.data['columns'].split(',')
            selected_headers = {i: columns[i] for i in range(0, len(columns))}
        else:
            columns = []
            selected_headers = {}
        mobile_ticket_reply = requests.get('http://localhost:8001/mobile_ticket_reply/').json()
        data = []
        header = {
            'Ticket_id': 'ticket_id',
            'message':'message',
            'send_by': 'send_by',
            'file_path':'file_path',
            'created_at':'created_at',
            'updated_at':'updated_at',

                 }

        mobile_ticket_reply_data = mobile_ticket_reply['results']
        for i in range(len(mobile_ticket_reply_data)):
            item = {
                   'mobile_ticket_reply_id': mobile_ticket_reply_data[i]['id'],
                   'message' : mobile_ticket_reply_data[i]['message'],
                   'send_by' : mobile_ticket_reply_data[i]['send_by'],
                   'file_path': mobile_ticket_reply_data[i]['file_path'],
                   'created_at': mobile_ticket_reply_data[i][ 'created_at'],
                   'updated_at' : mobile_ticket_reply_data[i]['updated_at'],
                    }
            mobile_ticket_response = dict(
                requests.get('http://13.232.166.20/mobile_ticket/' + str(mobile_ticket_reply_data[i]['id']) + '/', headers={'authorization': token}).json())
            item['ticket_id'] = mobile_ticket_response['ticket_id']
            data.append(item)
        new_data = []
        if len(data):
            serializer =ListMobileTicketReplySerializer(data, many=True)
            if len(columns) > 0:
                for obj in serializer.data:
                    columns.append('id')
                    columns.append('ticket_id')
                    new_item = {key: value for (key, value) in obj.items() if key in columns}
                    new_data.append(new_item)
                else:
                    new_data = serializer.data
                return Response({'count': mobile_ticket_reply['count'], 'next': mobile_ticket_reply['next'],
                                 'previous': mobile_ticket_reply['previous'],
                                 'header': header, 'selected_headers': selected_headers, 'data': new_data,
                                 'message': 'mobile_ticket_reply fetched successfully'})
        else:
            data = []
            return Response(
                {'count': 0, 'next': None, 'previous': None, 'header': header, 'selected_headers': selected_headers,
                 'data': data, 'message': 'No mobile_ticket_reply found'})


