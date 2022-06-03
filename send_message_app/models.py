from django.db import models


class Mailing(models.Model):
    start_datetime = models.DateTimeField()
    text = models.TextField()
    mark = models.CharField(max_length=255)
    end_datetime = models.DateTimeField()


class Client(models.Model):
    phone_number = models.IntegerField(unique=True)
    operator_code = models.CharField(max_length=255, blank=True)
    tag = models.CharField(max_length=255, blank=True)
    timezone = models.CharField(max_length=6)


class Message(models.Model):
    send_datetime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='message')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id', 'status')
