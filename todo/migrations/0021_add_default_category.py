# todo/migrations/0021_add_default_category.py

from django.db import migrations, models

def create_default_category(apps, schema_editor):
    Category = apps.get_model('todo', 'Category')
    default_category, created = Category.objects.get_or_create(name='Default Category')
    ShoppingItem = apps.get_model('todo', 'ShoppingItem')
    for item in ShoppingItem.objects.all():
        item.category = default_category
        item.save()

class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0020_shoppingitem_display_on_list'),  # 正しいマイグレーションファイル名を指定
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingitem',
            name='category',
            field=models.ForeignKey(default=1, on_delete=models.CASCADE, to='todo.Category'),
            preserve_default=False,
        ),
        migrations.RunPython(create_default_category),
    ]
