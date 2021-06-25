from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as v

from pre_campus_life import settings
from registration.forms import UserLoginForm
from .views import main_page, registration_page, going_to_event, going_to_event_detail, event_detail, \
    comments, create_event, edit_event, delete_event

app_name = 'events'

urlpatterns = [
    path('', main_page, name='main_page'),
    path(
        'login',
        v.LoginView.as_view(template_name="CampusLife/login.html",
                            authentication_form=UserLoginForm, ),
        name='login_page'),
    path('registration', registration_page, name='registration_page'),
    path('goint_to_event', going_to_event, name='going_to_event'),
    path('going_to_event_detail/<int:pk>', going_to_event_detail, name='going_to_event_detail'),
    path('event_detail/<int:pk>', event_detail, name='event_detail'),
    path('event-_etail/<int:pk>/comments', comments, name='comments'),
    path('create_event', create_event, name='create_event'),
    path('edit_event/<int:pk>', edit_event, name='edit_event'),
    path('delete_event/<int:pk>', delete_event, name='delete_event')
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
