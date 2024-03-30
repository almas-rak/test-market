from django.contrib import admin

from market.models.product_model import ProductModel
from market.models.category_model import CategoryModel

# Register your models here.
admin.site.register(ProductModel)
admin.site.register(CategoryModel)