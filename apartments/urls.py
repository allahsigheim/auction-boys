from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='apartments'),
    path('<int:apartment_id>/', views.detail, name='detail'),
    path('<int:apartment_id>/bid/', views.bid, name='bid'),
]