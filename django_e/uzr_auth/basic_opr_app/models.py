from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user_profile_model(models.Model):
    user = models.OneToOneField(User)
    # additiaonal classes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to = 'profile_pics',blank=True) #پروفایل پیکس  همان ساب دایرکتوری هست که باید فایل ها رو بفرسته

    def __str__(self):
        return self.user.username
        #user با حرف کوچیک یعنی از توی one to one میاد
        # حالا pillow رو توی محیط نصب میکنیم
        # تا بتونیماز عکس استفاده کنیم
                

'''pip install pillows'''