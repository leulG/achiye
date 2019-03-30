from django.db import models

# Create your models here.
class Structure(models.Model):
    Image  = models.ImageField(upload_to = 'Structure/img' , null = True , blank = True)
    pub_date = models.DateTimeField('date published' , auto_now_add=True )
    def __str__(self):
        return self.pub_date