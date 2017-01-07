from django import forms


class ArticleForm(forms.Form):
    url = forms.URLField(label='Article Url', required=True)
    tag = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 50}), max_length=16)


class SearchForm(forms.Form):
    query = forms.CharField(label='Enter a keyword to search for', widget=forms.TextInput(attrs={'size': 32, 'class': 'form-control'}))
