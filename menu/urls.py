from django.urls import path
from .views import index

urlpatterns = [path("menu", index, name="index")]
