from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Sneacers
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def reg(request):
    if request.method == 'POST':
        return redirect('/home')
    return render(request, 'main/index.html')


def home(request):
    return render(request, 'main/home.html')


def shop(request):
    sneacers = Sneacers.objects.all
    return render(request, 'main/shop.html', {'sneacers': sneacers})


@csrf_exempt
def neural_network(request):
    if request.method == 'POST':
        pass
    return render(request, 'main/neural_network.html')


def about(request):
    return render(request, 'main/about.html')
