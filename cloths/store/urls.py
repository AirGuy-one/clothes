from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('year/<int:yearid>/', views.year, name='year_url'),
    path('about/', views.about, name='about_url'),
    path('about/<int:itemid>/', views.item, name='item_url'),
    path('add/', views.adding, name='adding_url'),
    path('about_thing/', views.about_th, name='about_thing_url'),
    path('buy/<int:buyid>/', views.buy, name='buy_url'),
    path('support/', views.support, name='support_url'),
    path('basket/', views.basket, name='basket_url'),
    path('delete/<int:item_id>', views.delete, name='delete_url')
]
