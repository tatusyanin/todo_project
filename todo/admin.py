from django.contrib import admin
from .models import TodoItem, Category, ShoppingItem, Store

# admin.site.register(TodoItem) はコメントアウトまたは削除する
# admin.site.register(TodoItem)
admin.site.register(ShoppingItem)
admin.site.register(Category)

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'store', 'completed')
    list_filter = ('store', 'completed')
