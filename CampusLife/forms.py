from .models import Comments, Event
from django.forms import ModelForm, Textarea, ModelChoiceField


class AddComment(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment_text', ]
        widgets = {
            "comment_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст комментария',
                'rows': 9,
                'cols': 90,
            }),
        }


class AddEvent(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'event_img']
        widgets = {
            "title": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите заголовок события',
                'rows': 2,
                'cols': 90,
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание события',
                'rows': 8,
                'cols': 90,
                'resize': 'none',
            }),
        }
