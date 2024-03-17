from django.shortcuts import render

def Home(request):
    return render(request , 'Dreamdorms.html')

def base(request):
    return render(request , 'base.html')


# Create your views here.
