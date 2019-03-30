from django.db import models
from .validators import validate_file_extension
import datetime
from django.utils import timezone

# Create your models here.
class News(models.Model):
    Title    = models.CharField(max_length = 30)
    Sub_Title    = models.CharField(max_length = 40)
    Video    = models.FileField(upload_to = 'News/video/',null = True , blank = True,
               validators=[validate_file_extension])
    Image    = models.ImageField(upload_to = 'News/image/' , null = True , blank = True)
    Description = models.TextField()   
    pub_date = models.DateTimeField('date published' , auto_now_add=True )
    modified    =  models.DateTimeField('modified', auto_now_add=True)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    def __str__(self):
        return self.Title