from django.conf.urls import url
from django.views.generic import ListView
from restaurants.models import Food
from views import choose_town
from django.conf import settings

urlpatterns = [
    url('menu/', choose_town, name='menu'),
    ]
