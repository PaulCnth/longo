from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(label='Article Title', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'type keyword, then click search'}), required=True)
    url = forms.URLField(label='Article Url', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'https://www.google.com'}), required=True)
    content = forms.CharField(label='Article Content', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'abstract...'}), required=True)
    tag = forms.CharField(label='Tags', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'eg: Python,Django,Scala'}), max_length=100)


class SearchForm(forms.Form):
    query = forms.CharField(label='Enter a keyword to search for', widget=forms.TextInput(attrs={'size': 32, 'class': 'form-control'}))
