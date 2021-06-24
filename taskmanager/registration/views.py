from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, ProfileEditForm
from .models import Customers
from PIL import Image
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect


def main(request):
    return render(request, 'registration/main.html', {'title': 'Главная страница сайта'})


# def register(request):
#
#             user = authenticate(username=user_form.cleaned_data['username'],
#                                 password=user_form.cleaned_data['password'],
#                                 )
#             login(request, user)
#     form = DateForm(request.POST)
#     return render(request, 'registration/register.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST, request.FILES)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            if 'avatar' in request.FILES:
                new_user.avatar = request.FILES['avatar']

            new_user.set_password(user_form.cleaned_data['password'])

            new_user.save()
            user = authenticate(username=user_form.cleaned_data['username'],
                                password=user_form.cleaned_data['password'],
                                )
            login(request, user)
            return render(request, 'registration/main.html', {'user_form': user_form})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'crispy': user_form})


def prettify_image(file_path: str) -> None:
    img = Image.open(f"media/{file_path}")
    maxsize = (300, 300)
    img = img.resize(maxsize)
    print(f"media/{file_path}")
    img.save(f"media/{file_path}")


def customers_profile_view(request, username):
    user = Customers.objects.filter(username=username).values()
    user = user[0]
    prettify_image(user['avatar'])

    profile = {}
    ff = ['username', 'first_name', 'last_name', 'birthday', 'email', 'gender', 'course', 'inform']
    for item in user:
        if item in ff:
            profile.update({f'{item}': user[item]})

    return render(request, 'registration/profile.html', {'crispy': profile, 'user': user})


# @login_required
# def edit_profile_view(request, username):
#     if request.method == 'POST':
#         print(username)
#         edited_user = ProfileEditForm(request.POST, request.FILES)
#         user = Customers.objects.filter(username=username).first()
#         print(user)
#         if edited_user.is_valid() and user is not None:
#             print(edited_user.cleaned_data)
#             for cd_field in edited_user.cleaned_data:
#                 pass
#             edit_profile = user.save(commit=False)
#             if 'avatar' in request.FILES:
#                 edit_profile.avatar = request.FILES['avatar']
#             edit_profile.save()
#
#             messages.info(request, 'Your profile has been changed successfully!')
#             return render(request, 'registration/profile.html', {'crispy': edit_profile})
#     else:
#         edited_user = ProfileEditForm()
#     return render(request, 'registration/edit.html', {'crispy': edited_user})


def edit_profile_view(request, username):
    user_edit = Customers.objects.get(username=username)
    if request.method == 'POST':
        user_edit.first_name = request.POST.get("first_name")
        user_edit.last_name = request.POST.get("last_name")
        user_edit.email = request.POST.get("email")
        user_edit.course = request.POST.get("course")
        user_edit.inform = request.POST.get("inform")
        user_edit.save()
        return render(request, 'registration/profile.html', {'user_form': user_edit})

    else:
        user_edit = UserRegistrationForm()
    return render(request, 'registration/edit.html', {'crispy': user_edit})

# fn = request.POST["first_name"]
# ln = request.POST["last_name"]
#         em = request.POST["email"]
#         cour = request.POST["course"]
#         inf = request.POST["inform"]
#
#         print(username)
#         usr = Customers.objects.get_object_or_404(username=username)
#         usr.first_name = fn
#         usr.last_name = ln
#         usr.email = em
#         usr.course = cour
#         usr.inform = inf
#         usr.save()
#
#         edited_user.first_name = fn
#         edited_user.last_name = ln
#         edited_user.email = em
#         edited_user.course = cour
#         edited_user.inform = inf
#         edited_user.save()
#
#         context["status"] = "Change Saved Successfully"
#
#         return render(request, 'registration/main.html', context)
#     else:
#         new_user = ProfileEditForm()
#         return render(request, 'registration/edit.html', {'form': new_user})
