from django.urls import path
from . import views

urlpatterns = [
    path('', views.quote_list, name='quote_list'),
    path('random/', views.random_quote, name = 'random_quote')
]