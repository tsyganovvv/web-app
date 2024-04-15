from django.shortcuts import render, redirect
from .models import Sneacers
from .models import User
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def reg(request):
    error = ''
    if request.method == 'POST':
        password = request.POST['password']
        mail = request.POST['address']
        try:
            User.objects.get(mail=mail, password=password)
            return redirect('/home')
        except Exception:
            try:
                User.objects.get(mail=mail)
                error == 'Error'
            except Exception:
                User.objects.create(mail=mail, password=password)
                return redirect('/home')
    return render(request, 'main/index.html', {'error': error})


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
