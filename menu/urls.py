from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/", views.detail, name="detail"),
    path("<int:id>/edit", views.edit_dish, name="edit"),
    path("create/", views.create_dish, name="create"),
    path("<int:id>/delete", views.delete_dish, name="delete"),
]
