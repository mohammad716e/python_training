from django.db import models

# Create your models here.

class karbar(models.Model):

    fname= models.CharField(max_length=80)
    lname= models.CharField(max_length=80)
    email= models.EmailField(max_length=80,unique=True)

    def __str__(self):
        return f'{self.fname} {self.lname}'

