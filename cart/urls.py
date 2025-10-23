from django.urls import path
from . import views

app_name = 'cart'


urlpatterns = [
    path('detail/', views.CartView.as_view(), name='cart_detail'),
    path('add/<int:pk>', views.CartAddView.as_view(), name='cart_add'),

    path('remove/<str:id>', views.CartDeleteView.as_view(), name='cart_delete'),

    path('order/create', views.OrderCreateView.as_view(), name='order_create'),

    path('order/<int:pk>', views.OrderDetailView.as_view(), name='order_detail'),

    path('code/<int:pk>', views.DiscountCodeView.as_view(), name='code'),

]
