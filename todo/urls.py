from django.urls import path
from . import views


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
    path('logout-page/', views.logout_page, name='logout_page'),  # ログアウト後のページ用ビュー
    path('signup/', views.signup_view, name='signup'),  # 新規登録ページのURLを設定
    path('shopping/', views.shopping_todo, name='shopping_todo'),    # 買い物専用ページのパス設定
    path('calculate_total/', views.calculate_total, name='calculate_total'),
    ]
