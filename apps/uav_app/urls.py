from django.urls import path
from apps.uav_app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('iletisim/', views.contact, name='contact'),
    path('ucavs/', views.ucav, name='ucav'),
    path('ucavs/<int:pk>/', views.ucav_detail, name='ucav-detail'),

    path('ucavs/<int:pk>/rent/', views.rent_ucav, name='rent_ucav'),

    path('rentals/', views.list_rentals, name='list_rentals'),
    path('rentals/<int:pk>/edit/', views.edit_rental, name='edit_rental'),
]