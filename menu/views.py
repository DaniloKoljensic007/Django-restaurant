from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Dish

# Create your views here.


def index(request):
    dishes = Dish.objects.all()
    return render(request, "index.html", {"dishes": dishes})


def detail(request, id):
    try:

        dish = Dish.objects.get(id=id)

        dish_data = {
            "id": dish.id,
            "name": dish.name,
            "description": dish.description,
            "price": dish.price,
            "category": {"id": dish.category.id, "name": dish.category.name},
        }
    except Dish.DoesNotExist:
        return HttpResponse("This dish does not exist!")

    return render(request, "detail.html", {"dish": dish_data})
