from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='commercial_properties'),
    path('<int:commercial_id>/', views.detail, name='detail'),
]