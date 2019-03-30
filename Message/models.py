from django.db import models

from django.conf import settings
import datetime
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User , models.CASCADE , null = True , blank = True)
    message = models.TextField()
    time_stamp = models.DateTimeField('date sent' , auto_now_add = True)

    def __str__(self):
        return self.message