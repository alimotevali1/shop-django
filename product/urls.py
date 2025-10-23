from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('<int:pk>', views.Productdetail.as_view(), name='product-detail'),
    path('navbar', views.Nabvar.as_view(), name='navbar'),

    path('productslist', views.Productlist.as_view(), name='Productlist'),

]
