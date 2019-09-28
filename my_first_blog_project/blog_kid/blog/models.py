from django.db import models
from django.utils import timezone
# برای درست نوشتن زمان پست تایم زون رو میاریم
from django.core.urlresolvers import reverse
# برای ریدایرکت کردن به پیج  های دیگه هست

# Create your models here.
class Post(models.Model):

    authour = models.ForeignKey('auth.User') # برای  گرفتن یک یوزر به عنوان سوپر یوزر نویسنده پست هست 
    title = models.CharField(max_length = 300)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    publish_date = models.DateTimeField(blank=True,null=True)
    # or modified date
    
    def publish (self):
        self.publish_date = timezone.now()
        self.save()
    
    def approved_comments(self):
        self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse ('post_detail',kwargs={'pk':self.pk}) # خود متد reverse از اطلاعات داده شده بهش میتونه بسازه لینک رو 

    def __str__(self):
        return self.title

class comment(models.Model):
    post = models.ForeignKey('blog.post',related_name = 'comments')
    author_name = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now())
    approved_comment = models.BooleanField(default = False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    
    def __str__(self):
        return self.text

# تمام