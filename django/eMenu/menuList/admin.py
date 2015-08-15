from django.contrib import admin

from .models import Meal, Menu, Error

admin.site.register(Meal)
admin.site.register(Menu)
admin.site.register(Error)
