from django.shortcuts import render

# Create your views here.
from user_show.models import karbar



def index(request):
    return render(request,'user_show/index.html')


def users(request):
    UZR = karbar.objects.order_by('fname')
    dict={'insert_karbar': UZR }
    return render(request,'user_show/users.html',context=dict)