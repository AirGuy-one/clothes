from django.urls import path
from . import views

urlpatterns = [

    path('list/', views.ClothesListCreate.as_view()),
    path('create/', views.ClothesDelete.as_view()),
    path('detail/<int:pk>/', views.ClothsDetail.as_view()),

]
