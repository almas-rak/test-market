from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from market.models.product_model import ProductModel
from api.serealaizers.product_serialayzer import ProductSerializer

class ProductAPIView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = ProductModel.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
