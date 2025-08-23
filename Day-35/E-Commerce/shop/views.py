from rest_framework import viewsets
from .models import Customer, Product, Order
from .serializers import CustomerSerializer, ProductSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().prefetch_related('products').select_related('customer')
    serializer_class = OrderSerializer

class VersionedHelloView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            "message": f"Hello from API {request.version}"
        })