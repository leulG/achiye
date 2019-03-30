from django.db import models

# Create your models here.

from django.conf import settings
import datetime
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

class Sender(models.Model):
    Sender =  models.ForeignKey(User , models.CASCADE , null = True , blank = True )
    Text = models.TextField()
    
    TimeStamp = models.DateTimeField('date published' , auto_now_add=True )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return sender + '' + text
