from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.contrib import messages
from .models import Dish, Category, Order, OrderItem
from .forms import DishForm


# Create your views here.


def index(request, category_id=None):
    if not request.user.is_authenticated:
        messages.warning(request, "You must be login to access this page!")
        return redirect("login")

    else:
        categories = Category.objects.all()

        if category_id:
            selected_category = get_object_or_404(Category, id=category_id)
            dishes = Dish.objects.filter(category=selected_category)

        else:
            dishes = Dish.objects.all()
            selected_category = None

        return render(
            request,
            "index.html",
            {
                "dishes": dishes,
                "categories": categories,
                "selected_category": selected_category,
            },
        )


def detail(request, id):
    try:
        dish = Dish.objects.get(id=id)

        dish_data = {
            "id": dish.id,
            "name": dish.name,
            "description": dish.description,
            "price": dish.price,
            "category": {"id": dish.category.id, "name": dish.category.name},
            "is_available": dish.is_available,
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

    if not request.user.is_authenticated:
        messages.warning(request, "You must be logged in to access this page!")
        return redirect("login")

    if not request.user.is_staff:
        messages.error(request, "You don't have access to this page!")
        return redirect("index")

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


def order_dish(request, dish_id):

    if not request.user.is_authenticated:
        messages.warning(request, "You must be logged in to access this page!")
        return redirect("login")

    dish = get_object_or_404(Dish, id=dish_id)

    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))

        order = Order.objects.create(user=request.user)

        OrderItem.objects.create(order=order, dish=dish, quantity=quantity)

        return redirect("my_orders")
    return redirect("index")


def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "show_orders.html", {"orders": orders})
