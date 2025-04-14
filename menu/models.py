from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="dishes"
    )
    is_available = models.BooleanField(default=True)
