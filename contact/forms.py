from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(label='件名', max_length=100)
    sender = forms.EmailField(label='Email',required=False) #, help_text=''
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)
    myself = forms.BooleanField(label='同じ内容を受け取る', required=False)