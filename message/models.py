from django.db import models


class Message(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    status = models.BooleanField(default=False)
