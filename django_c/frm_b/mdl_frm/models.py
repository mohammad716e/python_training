from django.db import models

# Create your models here.
class subscriber(models.Model):
    name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254,unique=True)
    s_id = models.CharField(max_length=100,unique=True)

    def __srt__(self):
        return f'name :  {self.name} \n email : {self.email}'
