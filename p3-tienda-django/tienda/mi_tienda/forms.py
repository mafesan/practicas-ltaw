from django import forms

class SignUpForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_email = forms.CharField(label='Your email', max_length=100)

class SearchForm(forms.Form):
    search_text = forms.CharField(label='Busqueda', max_length=100)
