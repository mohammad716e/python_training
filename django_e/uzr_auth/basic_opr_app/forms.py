from django import forms
from django.contrib.auth.models import User
from basic_opr_app.models import user_profile_model

class User_reg_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    # تمام وییت ها آبجکت های متدی هستن که ریترن میشن
    # پس پرانتز دارن
    class Meta():
        model = User # دوباره از خود اوزر اثلی باحرف بزرگ گرفتیم
        fields= ('username','email','password')
# اینجا یدونه مدل فرم از خود یوزر ساختیم اما نمیدونم چرا دو فرم جدا از هم ساختیم و آیا یوزر حالا که 
# به صورت one to one با کلاس ما رابطه داره  آیا همین فرم به هر دو پر مدل یوزر و مدل 
# one to one شده از یوزر تبعیت میکنه یا نه
class user_profile_set_form(forms.ModelForm):
    class Meta():
        model = user_profile_model
        fields = ('portfolio_site','profile_pic')
