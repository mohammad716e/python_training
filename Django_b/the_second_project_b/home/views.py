from django.shortcuts import render

# Create your views here.
def home(request):
    my_dict={'msg':'سلام و درود ویژه بر شما که موقث شدید '}
    return render(request,'home/index.html',context=my_dict)