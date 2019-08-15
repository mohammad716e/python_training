from django.shortcuts import render
# کدی که ما اضافه کردیم
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = { 'insert_me' : "  امید وارم موفق باشید این پیام از جنگو است از طرف کانتکست"}
    # return HttpResponse("سلام از جنگو ")
    return render( request ,'first_app/index.html' , context = my_dict )

# def img(request):
#     my_con ={"hello":"mo"}
#     return render(request,'help/index.html', context = my_con)