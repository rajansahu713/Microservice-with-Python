from django.urls import path
from .views import BlogView

urlpatterns = [
    path('blogs/',BlogView.as_view(),name='product_list'),
]