from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.forms import UserCreationForm

from apps.cars.models import Car


def register(request):
    """Регистрация пользователя."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    """Профиль пользователя."""
    cars = get_list_or_404(Car, owner=request.user)
    return render(request, 'registration/profile.html',{'cars' : cars})
