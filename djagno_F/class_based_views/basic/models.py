from django.db import models

# Create your models here.
# حالا یک مدل تستی برای مدرسه و مدیر میسازیم
class school(models.Model):
    name = models.CharField(max_length=100)
    principal = models.CharField(max_length = 100 )
    location = models.CharField(max_length = 300 )
    
    def __str__(self):
        return self.name

class student ( models.Model):
    name = models.CharField(max_length = 100 )
    age = models.PositiveIntegerField()
    school = models.ForeignKey(school,related_name = 'students')
    def __str__(self):
        return self.name


# حالا کمی از اینا در ادمین استفاده میکنیم
# و یک سوپر یوزر میسازیم