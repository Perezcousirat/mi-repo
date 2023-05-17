from django.shortcuts import render

def index(request):
    return render(request, 'Miproyecto/index.html')
