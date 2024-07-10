# todo/admin.py

from django.contrib import admin
from .models import TodoItem, Category

admin.site.register(TodoItem)
admin.site.register(Category)


