from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'TeaTime_templates/base.html', {})

def index(request):
    return render(request, 'TeaTime_templates/index.html', {})

def bread_and_honey(request):
    return render(request, 'TeaTime_templates/bread_and_honey.html', {})

def flapjack(request):
    return render(request, 'TeaTime_templates/flapjack.html', {})

