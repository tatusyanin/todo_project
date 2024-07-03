from django.db import models

# Create your models here.
# todo/models.py


class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    description = models.CharField(max_length=100)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 価格フィールドを追加
    deadline = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=100)
    store_name = models.CharField(max_length=100, default="")  # 新しい store_name フィールドを追加

    def __str__(self):
        return self.title