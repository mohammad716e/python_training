""" 
                                                #  رفتن توی دایرکتوری که manage.py  هست
                                                #   رفتن توی environment
                                                #  python manage.py runserver

    django-admin startprojet esm_project_hala     #  ساخت کل یک پروژه ی جنگو
    python manage.py runserver                    # اجرای سرور
    python manage.py startapp eseme_app_pluggin   #  ساخت اپلیکیشن قابل پلاگ



    __init.py__  #  یک فایل خالی که با عث میشود کل دایرکتوری به عنوان پکیج شناخته شود
    settings.py  #  تمام تنظیمات در این فایل قرار میگیرد
    urls.py      #  برای لینک کردن قسمت های مختلف سایت 
    WSGI.py      #  وب سرور گیت وعی اینترفیس برای دیپلوی آنلاین
    manage.py    #  استفاده های بساری از این میشود و در واقع تغییرات اصلی را انجام میدهد

    ### برای ساخت اپلیکیشن که پلاگ بشه داریم

    python manage.py startapp app_name_here-->  نام اپ توی جنگو


    برای هر اپ جنگو داریم
    __init.py__   #  فایل خالی پایتول برای دسترسی به عنوان پکیج به این دایرکتوری
    admin.py      #  برای درست کردن یک اینترفیس ادمین 
    apps.py       #  هر نوع کانفیگ مخصوص برای هر اپی 
    models.py     #  برای ذخیره ی دیتا مدل های درون جنگو
    tests.py      #  توابعی برای تست کردن اپلیکیشن های درون جنگو
    views.py      #  برای ریترن کردن ریسپانس به هر یکوعست
    migrations    #  برای هر اپ اطلاعات مربوط به دیتا بیس را از مل ها میگیرد
"""
#==============================================================================================

"""
    معمولا ما برای هر اپلیکیشنی از مدل ها و ویو ها استفاده میکنیم

    1= بعد از ساختن هر اپی باید در ستیگ ها آن را وارد کنیم تا جنگو بداند نها ه هستند
    2= بعدن باید یک ویو ساخت وآن را به لینک در url مربوطط کرد تا کار کند

        1= python manage.py startapp first_app
        2= views from django.http import HtpResponse
        3=def index(request):
            return HttpResponse('سلام')
        3.5= وارد کردن اسم اپ در تنظیمات
            settings.py
            installed apps =[
                ,,,,,,
            ]
        4= urls.py
        5=from first_app import views
         add url
         utl(r'^$',views.index,name='index')
        6=python manage.py runserver
        به اینا میگم لینک دایرکت کردن
        
"""
#==============================================================================================
"""
    بریا لینک کردن به صورت ماژولار که هر اپی urls .py خودشو داشته باشه
    از تابع include در لایبری django.conf.urls لستفاده میشه تا url دزون هر پروژه هم به صورت ماژولار بیاد به 
    url اصلی

    1= urls.py in app_two
    2= in urls.py ...
    from django.conf.urls import url
    from app_two import views 
    
    urlpatterns = [
        url(r'^$',views.index,name='index')
    ]
    3=in project urls we use include
    from django.conf.urls import include
    4= in url we put ...
    url(r'^app_two',include('app_two.urls')),
    
"""
#==============================================================================================

"""
برای ساخت یک فولدر استاتسک برای نمایش هیمج ها 
    1= در روت یک فوادر به اسم روت درست میکنیم
    2= بعد در آن ایمج میگذاریم
    3= بعد در سینگ ها آن را وارد میکنیم
    STATIC_DIR = os.path.join(BASE_DIR,"static")
    3.1= در زیر STATIC_URL = '/static/' مینویسیم
    3.2= STATICFILES_DIRS = [
        STATIC_DRI,
    ]

    4= بعد در html 
"""