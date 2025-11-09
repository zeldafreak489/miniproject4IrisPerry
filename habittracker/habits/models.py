# INF601 - Advanced Programming in Python
# Iris Perry
# Mini Project 4

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class HabitRecord(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    completed_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.habit.name} - {self.completed_at.strftime('%Y-%m-%d $H:$M:%S')}"