from django.urls import path
from . import views
from .views import Home
from django.views.decorators.cache import cache_page
app_name = "Home"

urlpatterns = [
    path('', cache_page(60 * 1)(Home.as_view()), name='home'),
]