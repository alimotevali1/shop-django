from django.contrib import admin
from . import models


class OrderItemInline(admin.TabularInline):
    model = models.OrderItem



@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'address' , 'phone' , 'is_paid')
    inlines = (OrderItemInline,)
    list_filter = ('is_paid',)



@admin.register(models.Discountcode)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount' , 'quantity' )


# Register your models here.
