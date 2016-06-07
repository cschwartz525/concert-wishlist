from django import forms

class SearchForm(forms.Form):
    param_key = forms.CharField()
    param_value = forms.CharField()
    page = forms.CharField()
