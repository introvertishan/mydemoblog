from django import forms
from .models import *

class Blogform(forms.ModelForm):

    class Meta:
        model=Blogdata
        fields=['title','comment','pic']