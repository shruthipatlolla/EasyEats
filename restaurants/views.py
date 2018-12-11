# Create your views here.
from django.shortcuts import render, get_object_or_404
from restaurants.models import Food


def choose_town(request):
    food_list = Food.objects.all()
    print food_list
    return render(request, 'menu.html',
                  {'food_list': food_list})

