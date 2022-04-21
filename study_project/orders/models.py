from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from products.models import Product


class SalesOrder(models.Model):
    cost = models.IntegerField()
    amount = models.IntegerField()
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ManyToManyField(Product)

