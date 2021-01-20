from django.db import models
from twilio.rest import Client

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.email

    # def save(self, *args, **kwargs):
    #     account_sid = ''
    #     auth_token = ''
    #     client = Client(account_sid, auth_token)

    #     message = client.messages.create(
    #                     body=f'\nYooh Oliver, You\'ve a message on your site.\nIt was sent by {self.email}.\nSubject: {self.subject}.\nDescription: {self.description} ',
    #                     from_='',
    #                     to='+245799773244'
    #                 )
    #     print(message.sid)

    #     return super().save(*args, **kwargs)