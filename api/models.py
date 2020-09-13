from django.db import models
from django.utils import timezone


class ContactEmail(models.Model):
    username = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    subject = models.CharField(max_length=100, null=False, blank=False)
    contents = models.TextField(null=False, blank=False)
    send_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subject
