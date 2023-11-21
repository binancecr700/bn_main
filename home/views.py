from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def home(request, *args, **kwargs):
    return render(request, 'home/home.html', {})

