from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Habit, HabitRecord

def habit_list(request):
    habits = Habit.objects.all()
    return render(request, 'habits/habit_list.html', {'habits': habits})

def add_record(request, habit_id):
    habit = Habit.objects.get(id=habit_id)
    HabitRecord.objects.create(habit=habit, date=timezone.now().date())
    return redirect('habit_list')
