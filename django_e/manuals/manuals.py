
سلام در این پارت ما به این میپردازیم که چگونه یک اعتبارسنجی
در جنگو پیاده کنیم
    1 = در اپلیکیشن خود لایبری bcrypt رو نصب میکنیم
    با pip install
    2 = بعدن pip install django[argon2]
    که بعضا satisfied میشه
    3 = سپس در فایل خود یک متفیر از پیش تعیین شده به اسم
    PASSWORD_HASHERS را اور راید میکنیم ودر آن هشر های خود را 
    میریزیم
    PASSWORD_HASHERS = [
        'django.contrib.auth.hashers.Argon2PasswordHasher',
        'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
        'django.contrib.auth.hashers.BCryptPasswordHasher',
        'django.contrib.auth.hashers.PBKDF2PasswordHasher',
        'django.contrib.auth.hashers.PBKFD2SHA1PasswordHasher',
    ]
    که این به این معنی هست که در صورت کار نکردن اولی آرگون 2 به دومی بیکریپت بره
    و به همین ترتیب عقب نشینی کنه
    در ضمن همشون باید توی استرینگ باشن
    4 = بعد از اونا پسورد ولیداتور هست که به طور پیشفرض دز
    settings.py هست
    AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS':{'min_length':9}
    },


    5 = نکته برای آپلود های یوزر ها از media
    وبرای اپلود های خودمون از static استفاده میکنیم

    برای ساخت مدیا از مدیا روت استفاده میکنیم
    MEIA_ROOT = MEDIA_DIR
    MEDIA_URL = '/media/'
    اینطوری مدیا رو ست میکنیم
    
حالا که ادمین  و پسورد هشر ها رو آماده کردیم برای کار
وفت ساختن یک  فرم با استاده از آبجکت های یوزر هست

بجای اینکه مستقیم از آبجکت خود جنگو استفاده کنیم و از اون ارث ببریم
باید با یک رابطه ی one to one 
از آن اکستند کنیم
 البته اول مدل User 
 رو ایمپورت میکنیم
 from django.contrib.auth.models import User
 راستی دلیل اینکه نمیایم مستقیم ارث بری کنیم ولی one to one 
 میشه امنیت هست که اسکریپت نشه سایت 


#  =================================================
ساخت لاگین و لاگ آوت فیچر
USING DECORATORS
1= set up a login url 
    in settings files
like 
 LOGIN_URL = 'basic_opr_app/login.html'
 and in order to not shadowing the login variable 
 we use the user_login.html name for not shadowing
 