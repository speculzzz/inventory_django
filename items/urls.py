from django.contrib import admin
from django.urls import path
from . import views


app_name = 'items'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('item/<int:pk>/', views.ItemDetailView.as_view(), name='detail'),
    path('create/', views.ItemCreateView.as_view(), name='create'),
]
