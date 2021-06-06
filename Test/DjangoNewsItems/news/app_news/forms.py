from django import forms
from .models import NewsItem, Comment


class NewsItemCreateForm(forms.ModelForm):
    class Meta:
        model = NewsItem
        fields = '__all__'


class NewsCommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['name_author', 'text']
        widgets = {
            'name_author': forms.TextInput(attrs={'size': 20}),
            'text': forms.TextInput(attrs={'size': 30})
        }
