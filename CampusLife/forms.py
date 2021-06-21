from .models import Comments
from django.forms import ModelForm, TextInput, Textarea


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
