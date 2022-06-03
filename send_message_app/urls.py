from django.urls import path
from .views import ClientListAPIView, ClientCreateAPIView, ClientRetrieveUpdateDestroyAPIView, MailingListAPIView, MailingCreateAPIView, MailingRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('v1/client/create/', ClientCreateAPIView.as_view(), name='client_create'),
    path('v1/client/<int:pk>/', ClientRetrieveUpdateDestroyAPIView.as_view(), name='client_manage'),
    path('v1/client/', ClientListAPIView.as_view(), name='client'),
    path('v1/mailing/create/', MailingCreateAPIView.as_view(), name='mailing_create'),
    path('v1/mailing/<int:pk>/', MailingRetrieveUpdateDestroyAPIView.as_view(), name='mailing_manage'),
    path('v1/mailing/', MailingListAPIView.as_view(), name='mailing'),
]