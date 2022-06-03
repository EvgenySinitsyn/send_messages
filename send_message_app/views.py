from django.db.models import Q
from .serializers import ClientSerializer, MailingSerializer, MailingCreateSerializer
from .models import Client, Mailing, Message
from rest_framework import generics
from time import sleep
from getpass import getpass
import requests
import json
import datetime


class ClientCreateAPIView(generics.CreateAPIView):
    model = Client
    serializer_class = ClientSerializer


class ClientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientListAPIView(generics.ListAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class MailingCreateAPIView(generics.CreateAPIView):
    model = Mailing
    serializer_class = MailingCreateSerializer

    def create(self, request):
        response = super().create(request)
        clients = Client.objects.filter(Q(tag=response.data['mark']) | Q(operator_code=response.data['mark']))
        current_mailing = Mailing.objects.get(id=response.data['id'])
        for client in clients:
            Message.objects.create(status='not sent', mailing=current_mailing, client=client)
        return response


class MailingRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MailingSerializer
    queryset = Mailing.objects.all()


class MailingListAPIView(generics.ListAPIView):
    serializer_class = MailingSerializer
    queryset = Mailing.objects.all()


def send_messages():
    token = getpass("Введите токен для интеграции с внешним сервисом отправки сообщений: ")
    while True:
        sleep(5)
        now = datetime.datetime.now()
        mailings = Mailing.objects.filter(start_datetime__lte=now, end_datetime__gte=now)
        counter = 0
        for mailing in mailings:
            messages = Message.objects.filter(status='not sent', mailing=mailing)
            for message in messages:
                request_data = json.dumps(
                    {
                        "id": message.id,
                        "phone": message.client.phone_number,
                        "text": message.mailing.text
                    }
                )
                url = f'http://probe.fbrq.cloud/v1/send/{message.id}/'
                headers = {
                    'Authorization': token
                }
                response = requests.post(data=request_data, url=url, headers=headers)
                if response.status_code == 200:
                    print(f'message "{mailing.text}" to abonent "{message.client.phone_number}" is sent')
                    counter += 1
                    message.status = 'sent'
                    message.save()
        if counter == 0:
            print('There are no messages to send')
