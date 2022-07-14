from django.urls import path
from . import views

urlpatterns = {
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('closed', views.closed, name='closed'),
    path('open', views.open, name='open'),
    path('order', views.order, name='order'),
}
