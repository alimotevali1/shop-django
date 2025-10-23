from django.shortcuts import render
from django.views.generic import DetailView , TemplateView , CreateView , UpdateView , DeleteView , ListView

from product.models import Product , Category
from shop.settings import TEMPLATES


class Productdetail(DetailView):
    template_name = 'product/detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        infos = product.information.all()
        half = (infos.count() + 1) // 2
        context["half"] = half
        return context


class Nabvar(TemplateView):
    template_name = 'include/navbar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Categoryis"] = Category.objects.all()
        return context


class Productlist(ListView):
    template_name = "product/product_list.html"
    queryset = Product.objects.all()
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        request=self.request
        colors=self.request.GET.getlist('Colors')
        sizes=self.request.GET.getlist('size')
        min_price= self.request.GET.get('min_price')
        max_price= self.request.GET.get('max_price')
        queryset = Product.objects.all()

        if colors:
            queryset = queryset.filter(color__title__in=colors).distinct()

        if sizes:
            queryset = queryset.filter(size__title__in=sizes).distinct()

        if min_price:
            queryset = queryset.filter(price__gte=min_price).distinct()

        if max_price:
            queryset = queryset.filter(price__lte=max_price).distinct()

        queryset= queryset.filter(color__title__in=colors).distinct()
        context = super(Productlist,self).get_context_data()
        context["object_list"] = queryset
        return context




