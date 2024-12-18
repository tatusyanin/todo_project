from django.db import models

# Create your models here.
# todo/models.py

class Category(models.Model):#カテゴリ選択
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @staticmethod
    def default_category():
        return Category.objects.get_or_create(name='Default Category')[0]
    

class ShoppingCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # ショッピングカテゴリの説明

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    shopping_category = models.ForeignKey(ShoppingCategory, related_name='products', on_delete=models.CASCADE, null=True, blank=True)  # 新しいフィールド

    def __str__(self):
        return self.name    

class Store(models.Model):#店舗選択
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    description = models.CharField(max_length=100)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # 任意にする
    deadline = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_shopping = models.BooleanField(default=False)
    source = models.CharField(max_length=50, default='default')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)  # 店舗フィールドを追加
    quantity = models.IntegerField(default=1)  # ここに追加
    shopping_category = models.ForeignKey(ShoppingCategory, on_delete=models.CASCADE, null=True, blank=True)  # ショッピングカテゴリを追加する  # 新規フィールドを追加する  # 新規フィールドを追加する  # 新規フィールドを追加する  # 新規フィールドを追加する  # 新規フィールドを追加する

    def __str__(self):
        return self.title

class ShoppingItem(models.Model):
    item_name = models.CharField(max_length=100)
    prices = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)  # null=True, blank=Trueを追加
    display_on_list = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField(default=1)  # 個数フィールド　複数購入時
    shopping_category = models.ForeignKey(ShoppingCategory, on_delete=models.CASCADE, null=True, blank=True)  # ショッピングカテゴリを追加する  

    def __str__(self):
        return self.item_name
