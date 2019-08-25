from django import forms
from mdl_frm.models import subscriber

class new_form(forms.ModelForm):
    class Meta():
        model = subscriber
        fields = '__all__'