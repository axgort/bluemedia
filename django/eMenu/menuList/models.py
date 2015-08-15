from django.db import models


class Meal(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField()
    price = models.FloatField()


class Menu(models.Model):
    name = models.CharField(max_length=50, unique=True)
    meals = models.ManyToManyField(Meal, blank=True)


class Error(models.Model):
    details = models.TextField()
    email = models.EmailField(blank=True)
