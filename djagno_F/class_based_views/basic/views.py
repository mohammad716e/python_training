from . import models
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,ListView,DetailView,
                                  CreateView,DeleteView,UpdateView)
from django.shortcuts import render


# def index(request):
    # return render(request,'basic./index.html')

# class CBV_idx(View):
#     #  for getting method we have get method
#     def get(self,request):
#         return HttpResponse('<h1> سلام سلام بچه ها گل های خوب و زیبا  </h1>')
#         # این ویو فقط برای ویو هایی هست که قراره هیچ تمپلیتی رو نشون ندن و فقط 
#         # یک اچ تی پی ریسپانس نشون بدن
#         # برای ویو های دیگه از تمپلیت ویو ها استفاده مییشه


class temp_cbv_idx(TemplateView):
    template_name = 'basic/index.html' # اینجا هم باید یک یو آر ال داده بشه برحسب تمپلیت ویو ها
    # حالا برای کانتکست فرستادنش داریم
    def get_context_data(self,**kwargs): # *args برای تعداد المنت های توی پرانتز به کار میاد ولی

        '''# def foo(*args):
            # for a in args :
            #     print (a)
            # A خودکار از 1 شروع میشود
        # foo(1,2,4,9)
        # foo (1)
        # **kwargs برای  دیکشنری دادن به کار میاد
        # def bar(**kwargs):
            # for a in kwargs:
                # print (a, kwargs[a])
        # bar( name = "mohammad",age=21 )
        '''
        context = super().get_context_data(**kwargs)
        context['ins_msg'] = 'سلام از کانتکست داخل تمپلیت ویو'
        return context
        # اینم از نحوه ی استفاده از  کانتکست ویو باید زیاد تمرین بشه
#  حالا نحوه ی استفاده از ویو های کراد 
        
# که اکثر این ویو ها برای مدل ها تعریف میشه که 
# اتوماتیک تمام کارهای اصلی رو انجام میده برای نمایش و کانتکست وغیره
# قبلا با 
# Model.objects.all()----> context array 
# نمایش میدادیم ولی الان با استفاده از ویوهای خیلی خفن نمایش میدیم
#  این ویو ها انقدر توی جنگو مورد استفاده هستند که اصن کلاس خودشونو دارن
#  وreverse که یعنی هر تمپلتی داخل خود اپ باشه نه توی فولدر عمومی تمپلت 

                # THE REVERSE BEST PRACTICE
                # --------------------------
                

# حالا نوبت این رسیده که از کانونشن ریورس استفاده کنیم
# این یعنی که هر اپی برای خودش تمپلیت ویو داشته باشد و نه این که هر اپی در 
# فولدر تمپلیت اصلی یک ساب فولدر داشته باشد

# ======== in rooot ========
# ├───basic  ---------------> فولدر اپ
# │   ├───migrations
# │   │   └───__pycache__
# │   ├───templates --------> فولدر کانونشن تمپلیت ( new )
# │   │   └───basic --------> فولدر هم اسم اپ ( new )
# │   └───__pycache__
# ├───class_based_views
# │   └───__pycache__
# └───templates ------------> تمپلیت های عمومی
#     └───basic
 

class school_list_view (ListView):
    # here we connect the model
    model = models.school
    # and only this
    # و کانتکست رو خودش از روی مدل میسازه به این صورت که اسم مدل رو
    # به انتهای اون اضافه میکنه کلمه ی لیست رو با آندر اسکور
    # context = modelName_list
    # و برای اور راید کردن این تنظیمات از این خصیص استفاده میکنیم
    context_object_name = 'schools'

class school_detail_view (DetailView):
    model = models.school
    context_object_name = 'school_detail'
    template_name = 'basic/school_detail.html'

class students_list_view(ListView):
    model = models.school
    context_object_name = 'schools_data'


# داستان create view
# برای ساختن create view
#  باید اولن توجه داشت که نیازی به دادن آدرس تمپلیت نیست
# خودش توی ارور میگه که فلان تمپلیت رو پیدا نکرده و عین اونو میسازیم
# و اگر خواستیم تغییر میدیم با پراپرتی های خودش

class create_school_view(CreateView):
    fields =('name','principal','location')
    model = models.school