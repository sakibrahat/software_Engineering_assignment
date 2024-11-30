from django.urls import path
from app import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('create/', views.item_create, name='item_create'),
    path('update/<int:item_id>/', views.item_update, name='item_update'),
    path('delete/<int:item_id>/', views.item_delete, name='item_delete'),
]
