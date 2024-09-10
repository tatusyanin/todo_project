from django.urls import path
from . import views
from .views import shopping_todo, shopping_item_add, calculate_total_price



urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('create/', views.create_todo_item, name='create_todo_item'),
    path('delete/<int:todo_id>/', views.delete_todo_item, name='delete_todo_item'),
    path('edit/<int:todo_id>/', views.edit_todo_item, name='edit_todo_item'),
    path('toggle_completed/<int:todo_id>/', views.toggle_completed_status, name='toggle_completed_status'),
    path('todo-deleted/', views.todo_deleted, name='todo_deleted'),
    path('delete-cheapest-items/', views.delete_cheapest_items, name='delete_cheapest_items'),
    path('newly-added/<int:todo_id>/', views.newly_added_item_detail, name='newly_added_item_detail'),
    path('home/', views.home, name='home'),  # 'home'ビュー
    path('logout-page/', views.logout_page, name='logout_page'),  # ログアウト後のページ用
    path('signup/', views.signup_view, name='signup'),  # 新規登録ページのURLを設定
    path('shopping/', views.shopping_todo, name='shopping_todo'),    # 買い物専用ページのパス設定
    path('calculate_total/', views.calculate_total, name='calculate_total'),#合計額を計算
    path('shopping/create/', views.create_todo_item, name='shopping_item_todo1'),#作成
    path('shopping/add/', views.shopping_item_add, name='shopping_item_add'),#追加
    path('item/delete/<int:item_id>/', views.delete_shopping_item, name='delete_shopping_item'),
    path('shopping/calculate_total_price/', calculate_total_price, name='calculate_total_price'),
    ]
