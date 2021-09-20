from django import forms
from .models import CustomUser

 class BookForm(forms.ModelForm):
     class Meta:
         model = CustomUser
         fields = ('username')
         help_texts={
         'username':None,
         }