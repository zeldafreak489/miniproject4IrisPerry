from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('habits/', views.habit_list, name='habit_list'),
    path('habits/add/', views.add_habit, name='add_habit'),
    path('habits/<int:habit_id>/', views.habit_detail, name='habit_detail'),
    path('habits/<int:habit_id>/add/', views.add_record, name='add_record'),
    path('progress/', views.progress, name='progress'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]