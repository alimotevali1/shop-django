from django.db import models

from acount_app.models import User
from product.models import Product


class Order(models.Model):
    total_price= models.IntegerField(default=0)
    user= models.ForeignKey(User, on_delete=models.CASCADE  ,  related_name='orders')
    address=models.CharField(max_length=100)
    email=models.EmailField(blank=True, null=True)
    phone=models.CharField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name='items')
    size = models.CharField()
    color = models.CharField(max_length=3)
    quantity = models.IntegerField()
    price = models.PositiveIntegerField()



class Discountcode(models.Model):
    name= models.CharField(max_length=10, unique=True)
    discount=models.SmallIntegerField(default=0)
    quantity=models.SmallIntegerField(default=1)

    def __str__(self):
        return self.name









