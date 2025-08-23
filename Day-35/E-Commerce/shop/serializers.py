from rest_framework import serializers
from .models import Customer, Product, Order

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(), source='customer', write_only=True
    )
    products = serializers.StringRelatedField(many=True, read_only=True)
    product_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Product.objects.all(), source='products', write_only=True
    )

    class Meta:
        model = Order
        fields = ['id', 'customer', 'customer_id', 'products', 'product_ids', 'order_date', 'status']

    def create(self, validated_data):
        products = validated_data.pop('products', [])
        order = Order.objects.create(**validated_data)
        order.products.set(products)
        return order
