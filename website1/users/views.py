from django.shortcuts import render

def signup_view(request):
    return render(request, 'users/signup.html')
