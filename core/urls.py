from django.urls import path
from . import views

urls = [
    path('manufactures/', views.Manufactures.as_view(), name='manufactures'),
]
