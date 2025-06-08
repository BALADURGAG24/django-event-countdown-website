from django.urls import path
from . import views

urlpatterns = [
    path('', views.countdown_timer, name='countdown_timer'),
]
