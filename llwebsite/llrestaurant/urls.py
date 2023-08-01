from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('menu/<slug:slug>', views.ItemDetails.as_view(), name="menu-item"),
    path('reservations/', views.reservations, name="reservations"),
    path('thank-you/', views.thankyou, name="thank-you"),
]