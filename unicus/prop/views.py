from django.shortcuts import render, redirect
from django.http import HttpResponse


def redirect_view(request):
    response = redirect('https://one.exnesstrack.com/a/uaku4l8t')
    return response


def home(request):
    return render(request, 'unicusHome.html')


def register(request):
    return render(request, 'register.html')


