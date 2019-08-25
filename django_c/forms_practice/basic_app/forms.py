from django import forms
from django.core import validators


def check_for_z(val):
    if val[0].lower() != 'z':
        raise forms.ValidationError('man this is wrong use Z')
        print('not using z')

class my_form(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'inp'}),validators=[check_for_z])
    email = forms.EmailField() # widget=forms.TextInput(attrs={'class' : 'inp'})
    vrfmail = forms.EmailField(required=True)
    text = forms.CharField(widget=forms.Textarea(attrs = {'class':'inp'}))
    bot = forms.CharField(required=False,widget =forms.HiddenInput,validators=[
        validators.MaxLengthValidator(0)
    ])

    # def clean_bot(self):
    #     bot = self.cleaned_data['bot']
    #     if len(bot)>0 :
    #         raise forms.ValidationError(' hi man error ')
    #     return bot
    # این راه حل برای من raise error نداد اصلن
    # ولی راه دوم با vlidators هست

    # البته توی راه دوم هم ارورر فقط توی کنسول میده
    # راه سوم ولدیت کردن ایمیل
    def clean(self):
        # برای اینکه بفهمد فرم که یک ولیدیتور است از 
        # clean نام استفاده میکنیم بدون آندر اسگور
        all_clean_data = super().clean()
        # متد بسار مهم کلین که همیشه برای 
        # is_valid()
        # میشود تا بر اساس آن دیتا را لیبل  کنیم
        em = all_clean_data['email']
        vm = all_clean_data['vrfmail']
        if em != vm :
            raise forms.ValidationError("two emails must be identical")


