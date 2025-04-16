from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("category/<int:category_id>/", views.index, name="filter_by_category"),
    path("<int:id>/", views.detail, name="detail"),
    path("<int:id>/edit", views.edit_dish, name="edit"),
    path("create/", views.create_dish, name="create"),
    path("<int:id>/delete", views.delete_dish, name="delete"),
    path("order/<int:dish_id>", views.order_dish, name="order"),
    path("my_orders", views.my_orders, name="my_orders"),
]
