from django.conf.urls import urls
from . import views

app_name = 'users'

urlpatterns = [
    url(r'^signup/$', views.signup_view, name="signup")
]