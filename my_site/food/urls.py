from django import VERSION
from django.urls import path
from . import views

name = 'food'
urlpatterns = [
    path('', views.IndexClassView.as_view(), name="index" ),
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    path('add/', views.add_item, name='add'),
    path('edit/<int:item_id>/', views.edit, name='edit'),
    path('delete/<int:item_id>/', views.delete, name='delete'),
]