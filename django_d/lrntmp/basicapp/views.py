from django.shortcuts import render

# Create your views here.
def index(request):
    d = {'ins_text':'man i love me ' ,'ins_num':100}
    return render(request,'basicapp/index.html',d)

def other(request):
    
    return render(request,'basicapp/other.html',{'ins_title':'صفحه ی دیگر'})

def relative(request):
    print(request) # <WSGIRequest: GET '/basicapp/relative/'>
    return render(request,'basicapp/relative_url_template.html',{'ins_title':'صفحه ی وابسته'})