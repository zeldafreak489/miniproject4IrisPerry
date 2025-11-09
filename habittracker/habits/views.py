from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, HabitForm
from django.utils import timezone
from .models import Habit, HabitRecord
from django.db.models import Count

# Home View
def home(request):
    return render(request, 'home.html')

# User Registration
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Account created for {user.username}")
            return redirect('habit_list')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('habit_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout
def user_logout(request):
    logout(request)
    return redirect('home')

# Habits List for Each User
@login_required
def habit_list(request):
    habits = Habit.objects.filter(user=request.user)
    form = HabitForm()
    return render(request, 'habits/habit_list.html', {'habits': habits, 'form': form})

# Add Habit
@login_required
def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect('habit_list')
    return redirect('habit_list')

# Add HabitRecord
@login_required
def add_record(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    HabitRecord.objects.create(habit=habit, completed_at=timezone.now())
    return redirect('habit_list')

# Habit Detail
@login_required
def habit_detail(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user = request.user)
    records = HabitRecord.objects.filter(habit=habit).order_by('-completed_at')
    return render(request, 'habits/habit_detail.html', {'habit': habit, 'records': records})

# Progress Page
@login_required
def progress(request):
    data = HabitRecord.objects.filter(habit__user=request.user)\
        .values('habit__name')\
        .annotate(times_done=Count('id'))\
        .order_by('-times_done')
    return render(request, 'habits/progress.html', {'data': data})
