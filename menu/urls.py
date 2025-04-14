from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/", views.detail, name="detail"),
    path("edit/<int:id>/", views.edit_dish, name="edit"),
]
