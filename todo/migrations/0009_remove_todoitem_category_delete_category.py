# Generated by Django 5.0.6 on 2024-06-25 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_category_todoitem_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]