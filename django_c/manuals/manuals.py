
برای ساختن فرم های خود جنگو 
    1 = forms.py را دراخل اپ میسازیم
    2 = from django import forms درون آن مینویسیم 
    3 = در آن یک اینستنس ازکلاس فرم میسازیم
    class my_form ( forms.Form)
    سپس با استفاده از متد های خود فرم  درون آن را میسازیم
    5 = name = forms.CharacterField()
        email = forms.EmailField()
        text = forms.CharacterField(widget=Textarea)
    6 = حالا به ویو میرویم برای
        بعد از ساختن ویو برای ایندکس 
        def index(request):
            return render(request , 'pathhhh' )
        برای دیگر چیزمان یعنی فرم ویو میسازیم
        def frm_vw(request):
            حالا برای اینکه ما فرم نسازیم و بدیم خود تمپلیت تگینگ بسازه
            کلاس فرم رو که ساختیم یه اینستنس ازش میگیریم بعد میدیم
            اون اینستنس بجای دیکشنری کانتکست استفاده بشه
            ins_form = forms.my_form()
            return render (request , 'pathhhhhh' { 'ins_form': ins_form }) بله

    7 = و درآخر هم با یا بدون if میتونیم فرم رو نشون بدیم
        <html...........
        <form ..............
            {{ ins_form }}
        </form>
        البته تگ فرم دور این ساخته نشده پس خودمون دورش مینویسیم
        وبرای نشان دادن دریک پاراگراف از 
            {{ ins_form.as_p }}
        و البته سابمیت هم ساخنه نمیشه
        <input type='submit'/>
        و برای شخصی سازی کردن تم ها این ویدیو هم خوبه
        https://www.youtube.com/watch?v=_oMY2o2NhWM
    8 = البته برای فرم ها یا هرچیزی که از تمپلیت تگ استفاده میکنه باید دقت کرد به فاصله ها و 
        اینکه یک اسپیس اضافه زدن توی تمپلیت ها همه کار رو خراب میکنه

    9 = بعدا بعد از اینکه اطلاعات رو وارد کردیم میبنیم که بعد از سابمیت کردن هم هیچ چیزی نشد
        و ارور میده برای CSRF_TOken که برای اینه که 
        ریکوعست بروزر به ویو دوباره فرستاده بشه برای اینکه از
        ارورر جلوگیری بشه یک توکن ساخته میشه و بعد در صورت مچ بودن بررسی میشه
        برای انجام این کار باید در درون تگ 
        <form >
        نوشت {% csrf_token %} 
    10 = برای دریافت دیتا توی ویو باید جه کار کرد 
        1 = ابتدا نوشت اگر آبجکت ریکوعست اگر متدش برابر با
         پست بود که برای فرمه
         def hasan (request ):
            if request.method == post
            بجای اینکه خودمون بیام ریکوعست رو بشکنیم و آبکت ها
            رو دوباره بدیم به اغضای فرم به صورت جدا کل ریکوعست رو پاس میدیم به 
            اون آبجکت
            form = forms.my_form( request.post )
            و بعدا بررسی میکنیم که آیا فرم مقبول است یا نه
            B
            if form.is_valid()
            و بعدا با اطلاعات فرم به صوزت 
            print (form.cleaned_data['name'])
            اینطوری دست یابی پیدا میکنیم
            # در صورتی که is_valid()
            # فرا خوانی بشه cleaned_data['name']
            # و غیره رو داریم
            # print ("name : " + form.cleaned_data['name'])
            # # print ("email: " + form.cleaned_data['email'])
            # print ("text : " + form.cleaned_data['text'])
            # اگر ولید نباشه این آبجکت این متد را ندارد خوانده میشه


# ====================================================================

    validating the forms 
    1 = داخل خود فرم که در کلاس فرم نوشتیم 
        تمامی متدهایی که با  clean_ 
        شروع میشوند و بعد از آنها هر اسمی میاد به عنوان ولیدیتور به کار می روند

        def clean_bot_catch(self):
            if len(self.cleaned_data['botcatcher'])>0:
                then raie forms.validationError ( ' هز متنی دز اینجا میشه نوشت')
                forms. یعنی از کلاس اصلی در حال استفاده هستیم
#############################################################################
    bot = forms.CharField(required=False,widget =forms.HiddenInput,validators=[
        validators.MaxLengthValidator(0)
    ])

    # def clean_bot(self):
    #     bot = self.cleaned_data['bot']
    #     if len(bot)>0 :
    #         raise forms.ValidationError(' hi man error ')
    #     return bot
    # این راه حل برای من raise error نداد اصلن
    # ولی راه دوم با vlidators هست

    # البته توی راه دوم هم ارورر فقط توی کنسول میده


    2= یک راه دیگه برای ولید کردن دیتای توی سای هم هست
    یک تابع بسازیم با یک دستور رایز ارور وسپس به ولیدیتو ر پاش بدیم
        البته این تابع رو در بیرون از کلاس مینویسیم
    
def check_for_z(val):
    if val[0].lower() != 'z':
        raise forms.ValidationError('man this is wrong use Z')
        print('not using z')


        name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'inp'}),validators=[check_for_z])



    # البته توی راه دوم هم ارورر فقط توی کنسول میده
    # راه سوم ولدیت کردن ایمیل
    def clean(self):
        # برای اینکه بفهمد فرم که یک ولیدیتور است از 
        # clean نام استفاده میکنیم بدون آندر اسگور
        all_clean_data = super().clean()
        # متد بسار مهم کلین که همیشه برای 
        # is_valid()
        # میشود تا بر اساس آن دیتا را لیبل  کنیم
        em = all_clean_data['email']
        vm = all_clean_data['vrfmail']
        if em != vm :
            raise forms.ValidationError("two emails must be identical")
        




# =====================================================================================

    برای اینکه از مدل فرم بسازیم
    1 = مدل را میسازیم
    2= آن را در فرم ها ایمپورت میکنیم
    3= در کلاس متاتوی فرم می آوریم
    class new_form(forms.ModelForm):
    class Meta():
        model = subscriber
        fields = '__all__'
    
    4 = بعد فقط در ویو میمونه کانتکست سازی کردن

        def frm(request):

        form = new_form()
        if request.method == 'POST':
            form = new_form(request.POST)
            if form.is_valid():
                form.save(commit=True)
                return index(request)
            else:
                print('error from is not valid man ')

        return render(request,'mdl_frm/frm.html',{'ins_form':form})


# =============================================================

