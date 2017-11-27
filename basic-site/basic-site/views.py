from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('this is the homepage')
    return render(request, 'homepage.html')

def about(request):
    # return HttpResponse('an about page')
    return render(request, 'about.html')