from rest_framework import serializers
from .models import Client, Mailing, Message


class ClientSerializer(serializers.ModelSerializer):

    def validate_operator_code(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Operator_code contains only digits")
        elif value not in str(self.initial_data['phone_number']):
            raise serializers.ValidationError("Operator_code must be a part of phone_number")
        return value

    class Meta:
        model = Client
        fields = '__all__'


class MailingCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mailing
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(slug_field='phone_number', read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'status', 'client']


class MailingSerializer(serializers.ModelSerializer):
    message = MessageSerializer(many=True)

    class Meta:
        model = Mailing
        fields = '__all__'
