from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('artisan/', views.artisan_list, name='artisan_list'),
    path('register/', views.register_artisan, name='register_artisan'),
    path('detail/<int:artisan_id>/', views.artisan_detail, name='artisan_detail'),
    path('request-service/', views.request_service, name='request_service'),
    path('view-requested-services/', views.view_requested_services, name='view_requested_services'),
    path('success/', views.success, name='success'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
]
