from rest_framework import serializers
from .models import Department, Product, Order, Order_Product, Indicators, Profit_By_Hour, Dep_Pro_Profit

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'department']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'department_id', 'price', 'margin']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'order_hour_of_day']

class Order_ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Product
        fields = ['id', 'order_id', 'product_id', 'quantity']

class IndicatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicators
        fields = ['id', 'avg_tickets', 'avg_margin', 'avg_products_qty']

class Profit_By_HourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profit_By_Hour
        fields = ['id', 'hour_of_day', 'income', 'profit']

class Dep_Pro_ProfitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dep_Pro_Profit
        fields = ['id', 'department', 'product', 'profit', 'quantity']