from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.reviews_page, name='reviews_page'),
]
