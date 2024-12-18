from django.contrib import admin
from .models import TodoItem, Category, ShoppingItem, ShoppingCategory, Store, Product

# モデルの登録
admin.site.register(ShoppingItem)

# Category を重複登録しないようにする
if not admin.site.is_registered(Category):
    admin.site.register(Category)

admin.site.register(ShoppingCategory)

# Store モデルをカスタム登録
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name',)

# TodoItem モデルをカスタム登録
@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'store', 'completed', 'shopping_category')
    list_filter = ('store', 'completed', 'category', 'shopping_category')

# Product モデルをカスタム登録
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'shopping_category')  # 商品に関連するカテゴリを表示
    list_filter = ('category', 'shopping_category')  # カテゴリとショッピングカテゴリでフィルタリング
