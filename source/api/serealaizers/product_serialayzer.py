from rest_framework import serializers

from market.models.product_model import ProductModel
from api.serealaizers.category_seralizer import CategorySerializer




class ProductSerializer(serializers.ModelSerializer):
    product_categories = CategorySerializer(many=True)
    class Meta:
        model = ProductModel
        fields = [
            'id', 
            'product_image', 
            'product_name', 
            'product_categories', 
            'product_description',
            'product_qty',
            'product_price',
            'is_deleted',
            'created_at',
            'updated_at',
            'deleted_at'
            ]
        read_only_fields = [
            'id', 
            'is_deleted', 
            'created_at', 
            'updated_at', 
            'deleted_at'
            ]
