from django import forms
 
from ckeditor.widgets import CKEditorWidget # for Rich text editor
from Blog.models import *


# creating a form
class CreatePost(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget()) 


    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['cover'].widget.attrs['class'] = 'form-control'
        self.fields['tags'].widget.attrs['class'] = 'form-control'
        self.fields['category'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['class'] = 'form-control'
       
    class Meta:
        model = Posts
        fields = ('cover','title','category','tags','content')


