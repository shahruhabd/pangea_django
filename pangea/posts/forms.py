from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-control py-2'}))
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'class': 'form-control py-2'}))
    cost = forms.IntegerField(label='Цена (в тенге)', widget=forms.NumberInput(attrs={'class': 'form-control py-2'}))
    image = forms.FileField(label='Фото', widget=forms.ClearableFileInput(attrs={'class': 'form-control py-2'}))
    class Meta:
        model = Post
        fields = ('title', 'description', 'cost', 'image')
