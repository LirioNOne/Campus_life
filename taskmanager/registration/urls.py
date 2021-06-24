from django.urls import path
from django.contrib.auth import views
from taskmanager import settings
from .views import register, customers_profile_view, edit_profile_view
from .forms import UserLoginForm
from django.conf.urls.static import static
from .views import main

urlpatterns = [
                  path(
                      'login',
                      views.LoginView.as_view(template_name="registration/login.html",
                                              authentication_form=UserLoginForm, ),
                      name='login'),
                  path(
                      'logout',
                      views.LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL},
                      name='logout'),
                  path('register', register, name='register'),
                  path('change-password',
                       views.PasswordChangeView.as_view(template_name='registration/change-password.html',
                                                        success_url='change-password-done'),
                       name='change-password'),
                  path('change-password-done',
                       views.PasswordChangeDoneView.as_view(template_name='registration/change-password-done.html'),
                       name='change-password-done'),
                  path('main', main, name='main'),
                  path('edit/<username>', edit_profile_view, name='edit'),
                  path('profile/<username>', customers_profile_view, name='profile'),

                  path('', main, name='main_page'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
