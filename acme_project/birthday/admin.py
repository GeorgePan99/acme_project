from django.contrib import admin

from .models import Tag

# ...и регистрируем её в админке:
admin.site.register(Tag) 
