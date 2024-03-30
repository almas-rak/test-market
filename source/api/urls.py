from django.urls import path

from api.views.product_api_view import ProductAPIView


urlpatterns = [
    path('product/', ProductAPIView.as_view()),
]
