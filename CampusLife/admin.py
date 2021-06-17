from django.contrib import admin

from .models import CustomUser, Event, GoingToEvent

admin.site.register(CustomUser)
admin.site.register(Event)
admin.site.register(GoingToEvent)
