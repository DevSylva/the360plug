from django.contrib import admin
from django.urls import path
from .views import index, services, about, contact, sent

urlpatterns = [
    path('', index, name="index"),
    path('services/', services, name="services"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('messagesent/', sent, name="messagesent"),
]