"""
برای درست کردن مدل ها در جنگو داریم
    1=داخل هر app فایل models.py را باز میکنیم
    models.py
    2= و یک کلاس را بسازیم که از کلاس 
    models.Model ارث بری  میکند
    class topic(model,Model):
        topic_name=models.CharFeild( max_length = 264 , unique = True )
    3= معمولن همه ی کلاس ها به شکل استرینگ نوع پرینتشان را تعیین میکنیم
    def __str__(self):
        return self.topic_name
        یا str(self.topic_name) اگر عدد بود
    4= بعد از اینکه مدل ها رو ساختیم
        python manage.py migrate
        اولین بار چندتا ok ok میده
    5= بعدا python manage.py makemigrations esme_appi_ke_kar_mikonim
        تا migration ها رو بسازه
    6= و در نهایت دوباره 
        python manage.py migrate
    7= حالا مدل ها ساخته شدند و به دیتا بیس لینک شدند احتمالا
        و حالا میتوانیم با shell وار د آنها شویم و آنها را پر کنیم

"""
# SHELL IN PYTHON    WOW  LIKE IT

"""
SHELL IN PYTHON    WOW  LIKE IT
    # بعد از ساختن مدل ها برای بازی کردن با آنها باید از شل استفاده کنیم

    1= python manage.py shell
        شل اینتراکتیو پایتون رو برامون باز میکنه
    2= from esm_app_ma.models import folan_model

    3= print( folan_class_model.objects.all() )
        برای دیدن تمام اینستس ها ی ساخته شده از اون کلاس
        این فقط برای کلاس های جنگو هست نه برای کلاس های دیگه
        چون درواقع یه کوعری به دیتا بیس هست
        و در جوابش هم میاد
        <QuerySet [<Topic: social_network>]>
    
    4= t = Topic(topic_name='social_ network')
        برای اینکه یک اینستنس ساخته بشه با یک شکل اصلی

        دقت کنیم که برای تایپ کلاس نباید از
        t = Topic('social_network')
        استفاده کنیم چون اولین اتریبیوت در کلاس های ارث برده شده
        برای ما نیست پس باید تعریف کنیم که کدام کلاس اتریب را نام بردیم
        t = Topic(topic_name='social_ network')


"""
# now the admin panel

"""
and now THE ADMIN PANNEL
    برای اینکه هردفعه از شل استفاده نکنیم از ادمین خود سایت برای جنگو استفاده 
    میکنیم 
    برای اینکار باید همه ی  مدل ها رو توی  فایل ائمین اپ 
    رجیستر کنیم
    1 = داخل فایل ادمین آن اپلیکیشن میشویم
    2 = مدل ها را ایپورت میکنیم
    from my_app.models import model_hayi , ke_sakhtim
    3 = آنها را رجیستر میکنیم
    admin.site.register(avali)
    admin.site.register(dovomi)
    دونه به دونه باید رجیستر بشن
    نه توی یه خط
    5 = برای اینکه هر کسی نتونه بره از این دیتا استفاده کنه 
    یک ادمین میسازیم
    حد اقل باید یدونه بسازیم تا بعدا  بریم از توی خود ادمین بعدا
    کاربرهای مختلفی بسازیم

    6 = python manage.py createsuperuser
    و بعد موارد خواسته شده را پر میکنیم همشو
    
    7 = بعد از پر کردن همه ی موارد مینویسه که 
    Superuser created successfully.

    8 = حالا برای استفاده از ادمین باید به پیج ادمین بریم
    باید runserver کنیم 
"""
# ==================================================================
"""
استفاده از faker
    با اینکه استفاده از ادمین پنل خیلی راحت تر از شل بود
    اما برای دیتا های خیلی زیاد بهتره از اسکریپت  استفاده کنیم تادیتا 
    در سایت خود دیتا پاپیولیت کنیم
    پس لایبری faker را نصب میکنیم
    1 = pip install Faker

    داکیومنت خود فیکر را میشه دید تا نحوه ی استفاده شو دید
    
"""