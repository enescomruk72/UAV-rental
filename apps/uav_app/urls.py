from django.urls import path
from apps.uav_app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('iletisim/', views.contact, name='contact'),
    path('ihalar/', views.ucav, name='ucav')
]