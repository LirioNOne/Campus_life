from django.urls import path
from .views import main_page, login_page, registration_page, going_to_event, going_to_event_detail

app_name = 'events'

urlpatterns = [
    path('', main_page, name='main_page'),
    path('login', login_page, name='login_page'),
    path('registration', registration_page, name='registration_page'),
    path('goint_to_event', going_to_event, name='going_to_event'),
    path('going_to_event_detail/<int:pk>', going_to_event_detail, name='going_to_event_detail')
]