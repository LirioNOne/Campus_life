from django.contrib import admin
from .models import Customers


class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'birthday', 'course', 'inform', 'avatar', 'gender')


admin.site.register(Customers)
