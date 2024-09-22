from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from apps.cars.models import Car
from apps.cars.forms import CarAddForm
from apps.comments.forms import CommentForm


def index(request):
    """Главная страница со всеми автомобилями."""
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})


def car_detail(request, pk):
    """Сведения о конкретной машине."""
    car = get_object_or_404(Car, pk=pk)
    comments = car.comments.all()

    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.author = request.user
        comment.car = car
        form.save()
        return redirect('car-detail', pk=car.pk)
    else:
        form = CommentForm()
    return render(request, 'cars/car_detail.html',
                  {'car': car,
                   'comments': comments,
                   'form': form})


@login_required
def car_add(request):
    """Добавление автомобиля."""
    if request.method == 'POST':
        form = CarAddForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            form.save()
            return redirect('car-list')
    else:
        form = CarAddForm()
    return render(request, 'cars/car_add.html',
                  {'form': form})


@login_required
def car_delete(request, pk):
    """Удаление автомобиля."""
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        car.delete()
        return redirect('car-list')


@login_required
def car_edit(request, pk):
    """Изменение сведений автомобиля."""
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = CarAddForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car-detail', pk=pk)
    else:
        form = CarAddForm(instance=car)
    return render(request, 'cars/car_add.html',
                  {'form': form,
                   'car': car})
