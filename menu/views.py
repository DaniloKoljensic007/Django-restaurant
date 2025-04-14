from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Dish
from .forms import DishForm

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
        raise Http404("This dish does not exist!")

    return render(request, "detail.html", {"dish": dish_data})


def edit_dish(request, id):
    dish = get_object_or_404(Dish, id=id)

    if request.method == "POST":
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect("detail", id=dish.id)

    else:
        form = DishForm(instance=dish)

    return render(request, "edit.html", {"form": form})


def create_dish(request):

    if request.method == "POST":
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = DishForm()

    return render(request, "create.html", {"form": form})


def delete_dish(request, id):

    dish = get_object_or_404(Dish, id=id)
    dish.delete()
    return redirect("index")
