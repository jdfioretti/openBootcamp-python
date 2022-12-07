from django.shortcuts import render
from .models import *


def index(request):

    Directore = Directores.objects.all()

    return render(request, 'index.html', context={'Directores': Directore})
