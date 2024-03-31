from django.urls import path
from market import views

urlpatterns = [
    path("", views.ProductList.as_view(), name="main_page")
]
