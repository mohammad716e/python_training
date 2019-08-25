from django.shortcuts import render
from home.models import Webpage,Topic,Accessrecord

# Create your views here.
def home(request):
    Lizt = Accessrecord.objects.order_by('date')
    my_table = {'insert_table': Lizt }
    # دقت کنیم که در دیکشنری لزومن کلید استرینگ هست ولی والیوم نه
    # Lizt ار جنس آبجکته
    # my_dict={'msg':'سلام و درود ویژه بر شما که موقث شدید '}
    return render(request,'home/index.html',context=my_table)