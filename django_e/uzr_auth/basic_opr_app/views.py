from django.shortcuts import render
from basic_opr_app.forms import user_profile_set_form,User_reg_form
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib.auth import login , logout , authenticate








def index(request):
    return render ( request,'basic_opr_app/index.html')







@login_required
def uzr_logout(request):
    print('bfor lgout')
    logout(request)
    print ('log out ?')
    return HttpResponseRedirect(reverse('index'))






@login_required
def special(request):
    return HttpResponse(' آفرین به شما که لاگین کردید ')







def register(request):
    registered = False
    # return render ( request,'basic_opr_app/index.html')
    if request.method =="POST":
        # registered = False
        
        user_form = User_reg_form(data=request.POST)
        profile_form = user_profile_set_form(data=request.POST)
        # =====================================================
        if user_form.is_valid() and profile_form.is_valid():
            
            user =user_form.save()
            user.set_password(user.password)
            user.save()
            # ===========
            profile = profile_form.save(commit=False)
            profile.user = user
            # ===========
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            # ===========
            profile.save()
            registered =True
            # continue
        #     return render(request,'basic_opr_app/register.html',{
        #     'ins_form_reg':user_form,
        #     'ins_form_profile':profile_form,
        #     'registered':registered
        # })
        # دفعه اول ریترن رو زیر else نوشتم من uuuuu
        else: # NOT VALID
            print(user_form.errors,profile_form.errors)
            print("============================================")
            print("============== ERR ERR ERR =================")
            print("============================================")
        
        # ===============
    else: # REQUEST IS GET
        user_form = User_reg_form()
        profile_form = user_profile_set_form()
    return render(request,'basic_opr_app/register.html',{
        'ins_form_reg':user_form,
        'ins_form_profile':profile_form,
        'registered':registered
    })












def uzr_login (request):
    if request.method == 'POST':
        print('############################# post #############################')
        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user :
            print('############################# uzr #############################')
            
            if user.is_active: # is_active is not function
                print('############################# akt #############################')

                login(request,user)  # here the user is logged in now
                print('############################# success #############################')

                return HttpResponseRedirect(reverse('index')) #https://docs.djangoproject.com/en/2.2/ref/urlresolvers/
                # why use reverse
            else:
                print('############################# no akt #############################')

                return HttpResponse('این اکانت فعال نیست ')
        else:
            print('############################# no valid #############################')
            return HttpResponse(' اطلاعات شما برای لاگین درست نیست ')
    else:
        print('############################# no post #############################')
        return render(request,'basic_opr_app/login.html',{})
