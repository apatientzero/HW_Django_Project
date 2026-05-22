from django.shortcuts import render
from django.http import HttpResponse
import datetime
import os


def home_view(request):
    """Домашняя страница со списком доступных страниц"""
    context = {
        'pages': [
            {'name': 'Текущее время', 'url': '/current_time/'},
            {'name': 'Содержимое рабочей директории', 'url': '/workdir/'},
        ]
    }
    return render(request, 'home.html', context)


def current_time_view(request):
    """Показывает текущее время"""
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Текущее время: {formatted_time}")


def workdir_view(request):
    """Выводит содержимое рабочей директории"""
    workdir_path = os.getcwd()
    try:
        files_and_dirs = os.listdir(workdir_path)
        files_and_dirs.sort()

        result = f"<h1>Содержимое рабочей директории: {workdir_path}</h1>"
        result += "<ul>"
        for item in files_and_dirs:
            full_path = os.path.join(workdir_path, item)
            if os.path.isdir(full_path):
                result += f"<li><strong>[DIR] {item}</strong></li>"
            else:
                result += f"<li>[FILE] {item}</li>"
        result += "</ul>"

        return HttpResponse(result)
    except Exception as e:
        return HttpResponse(f"Ошибка при чтении директории: {str(e)}")