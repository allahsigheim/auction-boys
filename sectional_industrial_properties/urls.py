from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='sectional_industrial_properties'),
    path('<int:sectional_industrial_properties_id>/', views.detail, name='detail'),
]