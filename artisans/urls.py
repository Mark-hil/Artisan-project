from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('artisan/', views.artisan_list, name='artisan_list'),
    path('register/', views.register_artisan, name='register_artisan'),
    path('detail/<int:artisan_id>/', views.artisan_detail, name='artisan_detail')
]
