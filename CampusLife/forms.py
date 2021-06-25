from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

from .models import Comments, Event, CustomUser
from django.forms import ModelForm, Textarea, ChoiceField, CharField, PasswordInput, DateField, TextInput, \
    ImageField, Select, RadioSelect


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


class EditEvent(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditEvent, self).__init__(*args, **kwargs)
        to_return = {}
        for k, v in kwargs:
            to_return.update({k: v})
        return to_return


class AddEvent(ModelForm):
    event_img = ImageField()
    title = CharField(widget=Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Введите заголовок события',
        'rows': 2,
        'cols': 90,
    }))
    description = CharField(widget=Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Введите описание события',
        'rows': 8,
        'cols': 90,
        'resize': 'none',
    }))

    def __init__(self, *args, **kwargs):
        super(AddEvent, self).__init__(*args, **kwargs)

    class Meta:
        model = Event
        fields = ('title', 'description', 'event_img')
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


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = CharField()
    password = CharField(widget=PasswordInput)

    def clean(self):
        cd = self.cleaned_data

        if self.is_valid():
            user = authenticate(username=cd["username"], password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(self.request, user)
                else:
                    self.add_error('password', "passwords do not match !")

            else:
                self.add_error('username', 'user has not found')
        return cd


class UserRegistrationForm(ModelForm):
    password1 = CharField(label='Пароль', widget=PasswordInput)
    password2 = CharField(label='Повторите пароль', widget=PasswordInput)
    birthday = DateField(
        label='Дата рождения',
        widget=TextInput(attrs={'type': 'date'})
    )
    # GENDER = (
    #     ("Мужчина", "Мужчина"),
    #     ("Женщина", "Женщина")
    # )
    avatar = ImageField(label='Фото')
    # gender = ChoiceField(label='Пол', choices=GENDER, widget=Select())

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        # self.fields['gender'].required = False

    class Meta:
        model = CustomUser
        # fields = ('username', 'first_name', 'last_name', 'birthday', 'email', 'gender', 'course', 'inform', 'avatar')
        fields = ('username', 'first_name', 'last_name', 'birthday', 'email', 'course', 'avatar', 'inform')

    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password1'] != cd['password2']:
    #         raise ValidationError('Passwords don\'t match.')
    #     return cd['password2']
