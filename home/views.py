from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def home(request, *args, **kwargs):
    return render(request, 'home/home.html', {})


@csrf_exempt
def contact(request, *args, **kwargs):
    return render(request, 'home/contact.html', {})

