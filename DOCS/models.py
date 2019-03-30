from django.db import models
from .validators import validate_file_extension , vlalid_type
import datetime
from django.utils import timezone

# Create your models here.

Type_Choices = [ 
    ('type1' , 'TYPE1'),
    ('type2' , 'TYPE2'),
    ('type3' , 'TYPE3'),
    ('type4' , 'TYPE4'),]
    
class Document(models.Model):
    Type = models.CharField(max_length = 10 , choices = Type_Choices , default = 'Normal')
    Title    = models.CharField(max_length = 200)
    File     = models.FileField(upload_to = 'Document/files/', validators=[validate_file_extension])  
    Description = models.TextField()
    pub_date = models.DateTimeField('date published' , auto_now_add=True )
    modified    =  models.DateTimeField('modified', auto_now=True)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    def __str__(self):
        return self.Title
