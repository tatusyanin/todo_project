# todo/admin.py

from django.contrib import admin
from .models import TodoItem, Category
from .models import ShoppingItem, Category

admin.site.register(ShoppingItem)
admin.site.register(TodoItem)
admin.site.register(Category)


