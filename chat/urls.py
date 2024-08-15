from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('account/<str:room>/signupUser/', views.signupUser, name='signupUser'),
    path('account/<str:room>/loginUser/', views.loginUser, name='loginUser'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('account/<str:room>/', views.account, name='account'),
    path('getUser/<str:user>/', views.getUser, name='getUser'),
]