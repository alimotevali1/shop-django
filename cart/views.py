from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from product.models import Product
from .cart_detail import Cart
from .models import Order, OrderItem ,Discountcode
from django.conf import settings
import requests
import json


class CartView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, "cart/cart_detail.html", {"cart": cart})


class CartAddView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        size = request.POST.get("size","empty")
        color = request.POST.get("color","empty")
        quantity = request.POST.get("quantity", 1)

        # اعتبارسنجی داده‌های ورودی
        try:
            quantity = int(quantity)
            if quantity <= 0:
                quantity = 1
        except ValueError:
            quantity = 1

        if not size or not color:
            # اگه سایز یا رنگ انتخاب نشده باشه، می‌تونی یه پیام خطا بذاری
            return redirect("cart:cart_detail")

        cart = Cart(request)
        # ترتیب درست: product, quantity, color, size
        cart.add(product, quantity, color, size)

        return redirect("cart:cart_detail")

class CartDeleteView(View):
    def post(self, request, id):
        cart = Cart(request)
        cart.delete(id)   # الان متد وجود داره
        return redirect("cart:cart_detail")


class OrderDetailView(LoginRequiredMixin,View):
    def get(self, request ,pk):
        order = get_object_or_404(Order, id=pk)
        return render(request , 'cart/order_detail.html', {'order': order})

class OrderCreateView(LoginRequiredMixin,View):
    def get(self, request ):
        cart = Cart(request)
        order = Order.objects.create(user=request.user , total_price=cart.total())
        for item in cart:
            OrderItem.objects.create(order=order,product=item['product'],color=item['color'],size=item['size'], quantity=item['quantity'] , price=item['price'])
            cart.remove_card()

        return redirect("cart:order_detail", order.id)



class DiscountCodeView(LoginRequiredMixin,View):
    def post(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        code = request.POST.get("discount_code")
        discount_code = get_object_or_404(Discountcode, name=code)

        if discount_code.quantity == 0:
            return redirect("cart:order_detail", order.id)

        # چون discount به صورت عددی مثل 10 هست، باید درصدش رو حساب کنی
        order.total_price -= order.total_price * discount_code.discount/100
        order.save()
        discount_code.quantity -= 1
        discount_code.save()
        return redirect("cart:order_detail", order.id)


