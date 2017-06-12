from django import forms

from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_age = forms.CharField(label= 'Age')
    your_email = forms.EmailField(label = 'Email')
