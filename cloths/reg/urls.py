from django.urls import path, include
from . import views
from .views import LoginUser

urlpatterns = [

    path('', include('django.contrib.auth.urls')),
    path('login1/', LoginUser.as_view(), name='login_url'),
    path('reg/', views.register, name='register_url'),
    path('logout1/', views.logout_user, name='logout_url'),

]

