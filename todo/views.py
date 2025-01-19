
from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem, Category
from .forms import ToDoItemForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import TodoItem
from django.shortcuts import render
from .forms import ShoppingItemForm
from .models import ShoppingItem, Category
from .models import TodoItem, Store,Product

import logging

logger = logging.getLogger(__name__)
from .forms import DeckNameForm

@login_required
def home(request):
    deck_a_items = []
    deck_b_items = []
    deck_name = None
    lowest_price = None
    remaining_items = []

    if request.method == 'POST':
        form = DeckNameForm(request.POST)
        if form.is_valid():
            deck_name = form.cleaned_data['deck_name']
            # 入力されたデッキ名に基づいてアイテムをフィルタリング
            deck_items = TodoItem.objects.filter(deck_name=deck_name)
            
            # 最安値を計算
            if deck_items:
                lowest_price = min(item.price for item in deck_items)
                
                # 最安値と同じ価格の商品を残す
                remaining_items = [item for item in deck_items if item.price == lowest_price]

            return render(request, 'home.html', {
                'form': form,
                'deck_items': remaining_items,
                'deck_name': deck_name,
                'lowest_price': lowest_price
            })
    else:
        form = DeckNameForm()

    return render(request, 'home.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # ログイン後にリダイレクトするURLを設定
    return render(request, 'login.html')

@login_required
def todo_list(request):
    categories = Category.objects.all()
    todo_items = TodoItem.objects.all()  # 商品情報を全て取得
    # total_price = sum(todo.price or 0 for todo in todo_items)  # 値段の合計を計算
    # 合計金額を計算（price × quantity）
    total_price = sum(item.price * item.quantity for item in todo_items)
    selected_category = request.GET.get('category')  # URLパラメータでカテゴリを取得
    if selected_category:
        # カテゴリが選択されている場合、そのカテゴリの TodoItem をフィルタリング
        todo_items = TodoItem.objects.filter(category__name=selected_category)
    else:
        # カテゴリが選択されていない場合は全ての TodoItem を表示
        todo_items = TodoItem.objects.all()

    # ソート処理
    if 'sort_by_price' in request.GET:
        todo_items = todo_items.order_by('price')
    else:
        todo_items = todo_items.order_by('store__name')

    context = {
        'categories': categories,
        'todo_items': todo_items,  # 商品情報
        'total_price': total_price,  # 合計金額
    }

    return render(request, 'todo_list.html', context)


@login_required
def create_todo_item(request):
    if request.method == 'POST':
        form = ToDoItemForm(request.POST)
        if form.is_valid():
            todo_item = form.save(commit=False)
            todo_item.source = request.POST.get('source', 'default')
            todo_item.save()
            if todo_item.source == 'shopping':
                return redirect('shopping_todo')
            return redirect('todo_list')
    else:
        form = ToDoItemForm()
    categories = Category.objects.all()
    context = {
        'form': form,
        'stores': Store.objects.all()
    }
    return render(request, 'todo/create_todo_item.html', {'form': form, 'categories': categories})

@login_required
def mark_as_completed(request, todo_id):#完了ボタン
    todo_item = get_object_or_404(TodoItem, pk=todo_id)
    todo_item.completed = True
    todo_item.save()
    return redirect('todo_list')

def custom_logout_view(request):
    logout(request)
    return render(request, 'logout.html')

@login_required
def toggle_completed_status(request, todo_id):
    todo_item = get_object_or_404(TodoItem, pk=todo_id)
    todo_item.completed = not todo_item.completed
    todo_item.save()
    return redirect('todo_list')

@login_required
def todo_deleted(request):
    return render(request, 'todo/todo_deleted.html')

@login_required
def delete_todo_item(request, todo_id):
    todo_item = get_object_or_404(TodoItem, pk=todo_id)
    todo_item.delete()
    return redirect('todo_list')

@login_required
def edit_todo_item(request, todo_id):
    # 対象のTodoItemを取得
    todo_item = get_object_or_404(TodoItem, pk=todo_id)

    if request.method == 'POST':
        form = ToDoItemForm(request.POST, instance=todo_item)

        if form.is_valid():
            if 'add_new' in request.POST:
                # 新しいTodoItemを作成
                new_todo_item = form.save(commit=False)  # 保存前にインスタンスを取得
                new_todo_item.id = None  # 新しいIDを割り当てる
                new_todo_item.save()  # 新規保存
                return redirect('todo_list')  # ToDoリストにリダイレクト
            else:
                # 既存のTodoItemを更新
                form.save()
                return redirect('todo_list')  # ToDoリストにリダイレクト
    else:
        # GETリクエスト時にフォームを生成
        form = ToDoItemForm(instance=todo_item)

    # フォームをテンプレートに渡す
    return render(request, 'todo/edit_todo_item.html', {'form': form})

def newly_added_item_detail(request, todo_id):
    if request.method == 'POST':
        form = ToDoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shopping_todo_list')
    else:
        form = ToDoItemForm()
    todo_item = get_object_or_404(TodoItem, pk=todo_id)
    return render(request, 'todo/newly_added_item_detail.html', {'todo_item': todo_item})

@login_required
def delete_cheapest_items(request):  # 最安値を表示後削除
    items = TodoItem.objects.all()
    grouped_items = {}

    # 商品名ごとにアイテムをグループ化
    for item in items:
        if item.title:  # 商品名が存在する場合のみ
            if item.title not in grouped_items:
                grouped_items[item.title] = []
            grouped_items[item.title].append(item)
        else:
            # 商品名がないアイテムがある場合の処理（必要に応じて）
            print(f"Item without title: {item}")
    
    # 最安値以外のアイテムを削除
    for title, items in grouped_items.items():
        items.sort(key=lambda x: x.price if x.price is not None else float('inf'))  # Noneを最も高い値として扱う
        for item in items[1:]:  # 最安値のアイテムを除く
            item.delete()
    
    return redirect('todo_list')


def logout_view(request):
    if request.method == 'GET':
        return redirect('logout_page')  # GET メソッドの場合、logout_page ビューにリダイレクト
    logout(request)
    return redirect('home')  # ログアウト後にリダイレクトするURLを設定
def logout_page(request):
    """
    ログアウトページのビュー
    """
    logout(request)
    return redirect('home')  # ログアウト後のリダイレクト先を指定



from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):#サインアップ
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # サインアップ成功後にログインページにリダイレクト
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
from .models import ShoppingItem

def shopping_item_add(request):#買い物用
    if request.method == 'POST':
        form = ShoppingItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shopping_todo')  # リダイレクト先のURLネームを確認
        else:
            print(form.errors)  # エラーをコンソールに出力
    else:
        form = ShoppingItemForm()
    return render(request, 'shopping_item_add.html', {'form': form})

from .models import Category,ShoppingCategory
def shopping_todo(request):
    items = ShoppingItem.objects.all()
    shopping_categories = ShoppingCategory.objects.all()  # ショッピングカテゴリをすべて取得
    total_price = sum(item.prices * item.quantity for item in items if item.display_on_list)
    return render(request, 'shopping_todo.html', {'items': items, 'total_price': total_price,'shopping_categories': shopping_categories,})

def delete_shopping_item(request, item_id):#削除
    item = get_object_or_404(ShoppingItem, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('shopping_todo')
    return redirect('shopping_todo')

def calculate_total_price(request):#計算
    items = ShoppingItem.objects.all()
    total_price = sum(item.prices for item in items)
    return render(request, 'shopping_todo.html', {'items': items, 'total_price': total_price})

from django.shortcuts import redirect

def calculate_total(request):#合計額計算
    if request.method == 'POST':
        todos = TodoItem.objects.all()
        total_price = sum(todo.price for todo in todos)
        context = {
            'todos': todos,
            'total_price': total_price,
        }
        return render(request, 'todo_list.html', context)
    return redirect('todo_list')  # Todoリストページにリダイレクト

from .forms import DeckForm
from .forms import Deck

def create_deck(request):
    if request.method == 'POST':
        form = DeckForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')  # デッキ一覧ページへリダイレクト
    else:
        form = DeckForm()
    return render(request, 'search_app/create_deck.html', {'form': form})

def deck_list(request):
    decks = Deck.objects.all()
    return render(request, 'search_app/deck_list.html', {'decks': decks})
from django.db.models import Min

def deal_clear(request):
    # すべてのアイテムを取得
    items = todo_list.objects.all()
    
    # 最安値の価格を取得
    min_price = items.aggregate(Min('price'))['price__min']
    
    # 最安値の価格を持つアイテムを取得（デッキ名が異なる場合でも同じ最安値を残す）
    lowest_price_items = items.filter(price=min_price)
    
    # 最安値以外のアイテムを削除（最安値アイテムだけを残す）
    # 最安値のアイテムは削除せず、それ以外のアイテムを削除
    items.exclude(id__in=lowest_price_items.values('id')).delete()

    # 最安値アイテムとその価格を残す処理はここまでで行われる
    return redirect('todo_list')  # 適切なリダイレクト先に変更
