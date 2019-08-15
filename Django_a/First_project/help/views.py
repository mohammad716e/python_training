from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict_2 = { 'insert_me_2' : 'بسیار زیبا شما پیج دوم را هم درست کردید' }
    return render(request , 'help/index.html',context=my_dict_2)