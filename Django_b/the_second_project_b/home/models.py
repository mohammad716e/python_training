from django.db import models

# Create your models here.
# مثلا یک مدل برای اسم تاپیک ها در جنگو ساختیم

class Topic(models.Model):
    topic_name=models.CharField(max_length=264 , unique=True)

    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    # forign key برای ساخت ستون در کلاس جدید از کلاس دثگر یعنی همان دسته بندی کردن
    # فکر کنم یعنی این وب پیج هر تپیک که باشه از تاپیک های بالا بگیره
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class Accessrecord(models.Model):
    name = models.ForeignKey(Webpage)
    date = models.DateField()

    def __str__(self):
        return str(self.date)