from django.views.generic import ListView

from market.models import ProductModel


class ProductList(ListView):
    template_name = "market/index.html"
    model = ProductModel
    context_object_name = "products"

