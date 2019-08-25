from django.shortcuts import render
from basic_app import forms

def index(request):
    return render(request,'basic_app/index.html')

def my_form_view(request):
    if request.method == 'POST':
        print('psteeeeed')
        form = forms.my_form(request.POST)
        # print(form)
        # print ("name " + form.cleaned_data['name'])
        # print ("email" + form.cleaned_data [ 'email' ])
        # print ("text" + form.cleaned_data [ 'text' ])
        if form.is_valid():
            print(form.is_valid())
            print ("name : " + form.cleaned_data['name'])
            print ("email: " + form.cleaned_data['email'])
            print ("text : " + form.cleaned_data['text'])
        else :
            print(form.is_valid())
            # در صورتی که is_valid()
            # فرا خوانی بشه cleaned_data['name']
            # و غیره رو داریم
            # print ("name : " + form.cleaned_data['name'])
            # # print ("email: " + form.cleaned_data['email'])
            # print ("text : " + form.cleaned_data['text'])
            # اگر ولید نباشه این آبجکت این متد را ندارد خوانده میشه
    # حالا برای اینکه ما فرم نسازیم و بدیم خود تمپلیت تگینگ بسازه
    # کلاس فرم رو که ساختیم یه اینستنس ازش میگیریم بعد میدیم
    # اون اینستنس بجای دیکشنری کانتکست استفاده بشه
    ins_form = forms.my_form()
    return render(request, 'basic_app/form_page.html',{'ins_from':ins_form})