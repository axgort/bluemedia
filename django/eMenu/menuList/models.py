from django.db import models


class Meal(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField()


class Menu(models.Model):
    name = models.CharField(max_length=50, unique=True)
    meals = models.ManyToManyField(Meal)
    size = models.IntegerField()
