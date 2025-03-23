from django.urls import path
from . import views

app_name = 'home_base'

urlpatterns = [
    path('', views.home, name='home'),
]