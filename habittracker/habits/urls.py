from django.urls import path
from . import views

urlpatterns = [
    path('', views.habit_list, name='habit_list'),
    path('<int:habit_id>/add/', views.add_record, name='add_record'),
]