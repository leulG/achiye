from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.

import datetime
from django.utils import timezone

# Create your models here.
class Service(models.Model):
    Title       = models.CharField(max_length = 20)
    Sub_Title    = models.CharField(max_length = 30)
    Description = models.TextField(null = True , blank=True)   
    pub_date    = models.DateTimeField('date published' , auto_now_add=True)
    modified    =  models.DateTimeField('modified', auto_now=True)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    def __str__(self):
        return self.Title