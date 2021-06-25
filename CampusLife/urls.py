from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as v

from pre_campus_life import settings
from registration.forms import UserLoginForm
from .views import main_page, registration_page, going_to_event, going_to_event_detail, event_detail, \
    comments, create_event, edit_event, delete_event, customers_profile_view, edit_profile

app_name = 'events'

urlpatterns = [
                  path('', main_page, name='main_page'),
                  path(
                      'login',
                      v.LoginView.as_view(template_name="CampusLife/login.html",
                                          authentication_form=UserLoginForm, ),
                      name='login'),
                  path(
                      'logout',
                      v.LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL},
                      name='logout'),
                  path('change-password/<username>',
                       v.PasswordChangeView.as_view(template_name='CampusLife/change-password.html',
                                                    success_url='change-password-done'),
                       name='change-password'),
                  path('edit_profile/<username>', edit_profile, name='edit_profile'),
                  path('registration', registration_page, name='registration_page'),
                  path('going_to_event', going_to_event, name='going_to_event'),
                  path('going_to_event_detail/<int:pk>', going_to_event_detail, name='going_to_event_detail'),
                  path('event_detail/<int:pk>', event_detail, name='event_detail'),
                  path('event-_etail/<int:pk>/comments', comments, name='comments'),
                  path('create_event', create_event, name='create_event'),
                  path('edit_event/<int:pk>', edit_event, name='edit_event'),
                  path('delete_event/<int:pk>', delete_event, name='delete_event'),
                  path('profile/<username>', customers_profile_view, name='profile'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
