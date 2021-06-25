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
from django.shortcuts import render, redirect
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
        print(user_form)
        if user_form.is_valid():
            print(123)
            new_user = user_form.save(commit=False)
            print(user_form)
            if 'avatar' in request.FILES:
                new_user.avatar = request.FILES['avatar']

            new_user.set_password(user_form.cleaned_data['password'])

            new_user.save()
            print(new_user)
            user = authenticate(username=user_form.cleaned_data['username'],
                                password=user_form.cleaned_data['password'],
                                )
            login(request, user)
            return redirect('events:Main_page.html')
        else:
            user_form = UserRegistrationForm()
    return render(request, 'CampusLife/Registration_page.html', {'crispy': user_form})


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


@login_required
def edit_profile_view(request, username):
    if request.method == 'POST':
        print(username)
        edited_user = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        # user = Customers.objects.filter(username=username).first()
        # print(user)
        if edited_user.is_valid():
            edit_profile = edited_user.save(commit=False)
            if 'avatar' in request.FILES:
                edit_profile.avatar = request.FILES['avatar']
            edit_profile.save()

            messages.info(request, 'Your profile has been changed successfully!')
            return render(request, 'registration/main.html', {'crispy': edited_user})
    else:
        edited_user = ProfileEditForm()
    print(username)
    return HttpResponseRedirect(f'edit/{username}')

# class EditProfileView(generic.CreateView):
#     model = Customers
#     template_name = 'registration/edit.html'
#     fields = ['first_name', 'last_name', 'email', 'course', 'inform', 'avatar']
#     success_url = reverse_lazy('main')
#
#     def get_object(self):
#         return self.request.Customers


# def edit_profile_view(request, username):
#     context = {}
#     edited_user = ProfileEditForm(request.POST, request.FILES)
#     context["data"] = edited_user
#     if request.method == 'POST':
#         fn = request.POST["first_name"]
#         ln = request.POST["last_name"]
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
