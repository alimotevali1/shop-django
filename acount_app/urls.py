from django.urls import path
from . import views

app_name = 'account_app'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('address/', views.Addessview.as_view(), name='address'),
]
