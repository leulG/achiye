from django.db import models

# Create your models here.
from .validators import validate_file_extension 
from django.conf import settings
import datetime
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

# Create your models here.

    
class JobOrder(models.Model):
    user =  models.ForeignKey(User , models.CASCADE , null = True , blank = True )
    Title    = models.CharField(max_length = 200)
    File     = models.FileField(upload_to = 'Users_File/files/', validators=[validate_file_extension] , null = True , blank = True)  
    Description = models.TextField()
    pub_date = models.DateTimeField('date published' , auto_now_add=True )
    @property
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
   
    def __str__(self):
        return self.Title


