from django.contrib import admin

from .models import Event, GoingToEvent, Comments, CustomUser

admin.site.register(Event)
admin.site.register(GoingToEvent)
admin.site.register(Comments)
admin.site.register(CustomUser)
