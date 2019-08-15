from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse(" <strong> سلام بزرگ از جنگو پروژه ی 2 <strong> ")

def help(request):
    help_dict={'insert_help': ' من از طرف یک ویو برای کمک در نرم افزار طراحی شدم '}
    return render(request, 'app_two/help.html' , context=help_dict )