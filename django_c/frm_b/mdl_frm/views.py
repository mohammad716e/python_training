from django.shortcuts import render
from mdl_frm.forms import new_form

# Create your views here.
def index(request):
    return render(request,'mdl_frm/index.html')

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
