from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Category, Product, Cart, CartProduct
from .serializers import CategorySerializer, ProductSerializer, CartSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def add_product(self, request, pk=None):
        product_to_add = get_object_or_404(Product, pk=pk)
        cart = self.get_object()
        cart.products.add(product_to_add)
        cart.save()
        return Response({'status': 'product added'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def change_quantity(self, request, pk=None):
        cart_product = get_object_or_404(CartProduct, pk=pk)
        quantity = request.data.get('quantity', 1)
        cart_product.quantity = quantity
        cart_product.save()
        return Response({'status': 'quantity updated'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['delete'], permission_classes=[IsAuthenticated])
    def remove_product(self, request, pk=None):
        product_to_remove = get_object_or_404(Product, pk=pk)
        cart = self.get_object()
        cart.products.remove(product_to_remove)
        cart.save()
        return Response({'status': 'product removed'}, status=status.HTTP_200_OK)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    pagination_class = StandardResultsSetPagination


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    pagination_class = StandardResultsSetPagination
