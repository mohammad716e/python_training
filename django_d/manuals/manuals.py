'''
    ------------------------------------------------------------------
    سلام
    نکته 
    اول اینکه در این قسمت شرت کات درون خود وی  اس کد برای درست 
    کردن فایل رو پیدا کردم
    ctrl + shift + p خط فرمان
    new file نوشتن 
    و اسم دادن در هر جای 
    ctrl + b که باشیم
    و روش دیگر در 
    ctrl + b که میرویم 
    دکمه ی راست کلیک رو میزنیم
    و delete و create new file و create new folder  
    هم موجوده
    ------------------------------------------------------------------

    بعد نکته ی دوم اینه که در جنگو همیشه باید جینجا ها رو دقت کرد
    خیلی با یدونه فاصله اذیت میکنه یعنی مثلا توی نوشتن هر چیزی
    که نوعی لینک هست اگر بین single qoutes
    یدونه اسپیس باشه اسم رو نمیفهمه میره دنبال اسم اسپیس دار میگرده
    ------------------------------------------------------------------

'''
# ===========================================================================================
'''
    RELATIVE VIEWS
    -----------------------------------------------------------------
    app_name = 'esme_app' # این یک خط خطی است که به ما اجازه میدهد تا 
    # از تمپلیت لینکینگ استفاده کنیم
    و در urls .py این ثابت را مینویسیم
    و علاوه بر اون این name که در آخر 
    url() میاد برای تمپلیت تگینگ هست
        url(r'^relative/$',views.relative,name='relative') # name is for templat tagging

    -----------------------------------------------------------------
    نکته 
        def relative(request):
        print(request) # ================>> <WSGIRequest: GET '/basicapp/relative/'>
        return render(request,'basicapp/relative_url_template.html')
    -----------------------------------------------------------------
    و در نهایت ما برای ادمین و هر اپی که هست و ساختیم با تمپ تگ لینک میدیم
     <a href="{% url 'admin:index' %}">LINK TO ADMIN</a>            <span> == </span>

        البته باید بدونید برای اپ ادمین باید مایگریت ه انجام بشه

    <a href="{% url 'index' %}">LINK TO INDEX</a><span> == </span>

        برای خود ایندکش هم استثنا هست

    <a href="{% url 'basicapp:other' %}">LINK TO OTHER</a><span> == </span>
    <a href="{% url 'basicapp:relative' %}">LINK TO RELATIVE</a><span> == </span>
    </body>
    
'''

# ===========================================================================================

'''
        TEMPLATE INHERITANCE
    --------------------------------------------------------------------------
    معمولا در صفحه ای به نام base.html
    ما میاییم و یک پیج اصلی که تک اصلی سایت کا را در بردارد طراحی میکنیم و در آن محلی برای
    پلاگ کردن دیگر html های خود قرار میدهیم
    <!DOCTYPE html>
    {% extends 'basicapp/base.html' %}

    {% block body_block %}
     our code here !!!!!
    {% endblock %}
'''

# ==========================================================================================

'''
    FILTERS IN JINJA
    --------------------------------------------------------------------------
        <h2 dir="ltr">{{ ins_text|upper }} | upper </h2> 
        <h2 dir="ltr">{{ ins_num|add:3562 }} | add "3562" </h2></dir>
        فقط به داک خود این ها مراجعه میکنیم و اگر خواستیم کاستوم بسازیم داریم
        1 = در اپ خود یک فولدر به اسم templatetags
        2 = داخل این فولدر یک فایل به اسم __init__.py میسازیم
        3 = سپس فایلی به اسم دلخواه ساختع hasan.py
        4 = register ها رو ایمپورت میکنیم
        5 = تابع رو مینویسیم
        6 = به رجیستر فیاتر میدیمش
        7 = فیلتر ذو استفاده میکنیم
        from django import template

        register = template.Library() # register بود یا reg فرق نداره


        def cut_the(value,arg):
            return value.replace(arg,'')

        register.filter('cut',cut_the)
        یا با دکوریتور بدیم بره به رجیستر

'''