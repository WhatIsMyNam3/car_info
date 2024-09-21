from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from apps.cars.models import Car
from apps.comments.forms import CommentForm


def index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})


def car_detail(request, pk):
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
