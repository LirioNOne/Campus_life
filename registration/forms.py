from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login
from django.forms import ModelForm, Textarea
from .models import Customers
from .widgets import FengyuanChenDatePickerInput


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

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


class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    old_password = forms.PasswordInput()
    new_password1 = forms.PasswordInput()
    new_password2 = forms.PasswordInput()

    def clean(self):
        u = Customers.objects.get(username=self.request.user)
        if self.request.method == 'POST':
            form = ChangePasswordForm(self.request.POST)
            if form.is_valid():
                old_password = self.request.POST.get("old_password")
                new_pass = self.request.POST.get("new_password1")
                new_pass_rep = self.request.POST.get("new_password2")
                from django.contrib.auth.hashers import check_password
                if not check_password(old_password, u.password):
                    self.add_error('old_password', 'Old password is wrong')
        else:
            form = ChangePasswordForm()


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    birthday = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'})
    )
    avatar = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None

    class Meta:
        model = Customers
        fields = ('username', 'first_name', 'last_name', 'birthday', 'email', 'gender', 'course', 'inform', 'avatar')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class CustomersProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomersProfileForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Customers
        fields = ('username', 'first_name', 'last_name', 'birthday', 'email', 'gender', 'course', 'inform')

    def clean(self):
        cd = self.cleaned_data
        return cd


class ProfileEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)

    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    course = forms.CharField(max_length=2)
    inform = forms.TextInput()

    class Meta:
        model = Customers
        fields = ['first_name', 'last_name', 'email', 'course', 'inform']

#
#     def clean(self):
#         cd = self.cleaned_data
#         return cd
