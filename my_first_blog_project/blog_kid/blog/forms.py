from django import forms
from blog.models import Post,comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('auther', 'title','text')
        widget = {
            'title': forms.TextInput(attrs = {'class':'textinputclass'}),
            'text': forms.Textarea(attrs = {'class':' editable medium-editor-textarea postcontent'})
        }
class commentForm(forms.ModelForm):

    class Meta():
        model = comment
        fields = ('text','auther')
        widgets = {
            'author':forms.TextInput(attrs = {'class': 'textinputclass'}),
            'text': forms.Textarea(attrs = {'class':' editable medium-editor-textarea'})
        }
        