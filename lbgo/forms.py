from django import forms


class ArticleForm(forms.Form):
    url = forms.URLField(label='Article Url', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg: https://www.google.com'}), required=True)
    tag = forms.CharField(label='Tags', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg: Python,Django,Scala'}), max_length=100)


class SearchForm(forms.Form):
    query = forms.CharField(label='Enter a keyword to search for', widget=forms.TextInput(attrs={'size': 32, 'class': 'form-control'}))
