from django import forms
from .models import TodoItem, Category


class ToDoItemForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d', '%Y/%m/%d', '%Y年%m月%d日']
    )

    PRIORITY_CHOICES = [
        ('低', '低'),
        ('中', '中'),
        ('高', '高'),
        ('まじ高い', 'まじ高め'),
        ('最速でやれよ','最速でやれよ')
    ]
    priority = forms.ChoiceField(choices=PRIORITY_CHOICES)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="選択してください",
        to_field_name='name'
    )
    class Meta:
        model = TodoItem
        fields = ['description', 'due_date', 'priority', 'price','store_name', 'category','is_shopping']
        