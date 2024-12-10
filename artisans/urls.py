from django.urls import path
from . import views

urlpatterns = [
    path('', views.artisan_list, name='artisan_list'),
    path('register/', views.register_artisan, name='register_artisan'),
    path('detail/<int:artisan_id>/', views.artisan_detail, name='artisan_detail')
]
