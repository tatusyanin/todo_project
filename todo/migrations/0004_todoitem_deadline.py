# Generated by Django 5.0.6 on 2024-05-24 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todoitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]