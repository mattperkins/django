from django.http import HttpResponse

def homepage(request):
    return HttpResponse('this is the homepage')

def about(request):
    return HttpResponse('an about page')