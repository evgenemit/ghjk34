from django.shortcuts import render

from .models import Record


def home(request):
    """Главная страница"""

    return render(request, 'json_processing/home.html')


def result(request):
    """Страница записей"""

    records = Record.objects.all()
    return render(request, 'json_processing/result.html', {'records': records})
