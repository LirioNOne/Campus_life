from django.contrib import admin

from .models import CustomUser, Event, GoingToEvent, Comments

admin.site.register(CustomUser)
admin.site.register(Event)
admin.site.register(GoingToEvent)
admin.site.register(Comments)
