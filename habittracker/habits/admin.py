# INF601 - Advanced Programming in Python
# Iris Perry
# Mini Project 4

from django.contrib import admin
from .models import Habit, HabitRecord

admin.site.register(Habit)
admin.site.register(HabitRecord)
