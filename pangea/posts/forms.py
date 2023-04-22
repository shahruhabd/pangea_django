from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-input'}))
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'class': 'form-input form-input_desc'}))
    cost = forms.IntegerField(required=False, min_value=None, label='Цена (в тенге)', widget=forms.NumberInput(attrs={'class': 'form-input'}))
    image = forms.FileField(label='Фото', widget=forms.ClearableFileInput(attrs={'class': 'form-image form-control'}), required=False)
    class Meta:
        model = Post
        fields = ('title', 'description', 'cost', 'image')


class PostDeleteForm(forms.Form):
    is_rent = forms.BooleanField(label='Вы сдали квартиру?', required=False)
