from django import forms

from .models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'publication_date', 'body_text', 'image')
