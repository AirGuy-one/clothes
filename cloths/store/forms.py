from .models import ClothsData, CategoryData, Like
from django.forms import ModelForm, TextInput, ModelChoiceField, ChoiceField


class ClothsDataForm(ModelForm):
    class Meta:
        model = ClothsData
        fields = ('title', 'color', 'price', 'photo', 'cat', 'user')
        labels = {
            'title': 'this is label of title',
            'color': '',
            'price': '',
            'photo': '',
            'cat': '',
            'user': ''
        }
        # widgets = {
        #     "title": TextInput(attrs={
        #         "class": "form-control",
        #         "placeholder": "Введите название"
        #     }),
        #     "color": TextInput(attrs={
        #         "class": "form-control",
        #         "placeholder": "Введите цвет"
        #     }),
        #     "price": TextInput(attrs={
        #         "class": "form-control",
        #         "placeholder": "Введите цену",
        #         'type': 'number'
        #     }),
        # }


class DeleteForm(ModelForm):
    class Meta:
        model = ClothsData
        fields = []


class LikeForm(ModelForm):
    class Meta:
        model = Like
        fields = ['user', 'post', 'value']





