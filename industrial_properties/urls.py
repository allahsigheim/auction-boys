from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='industrial_properties'),
    path('<int:industrial_properties_id>/', views.detail, name='detail'),
]