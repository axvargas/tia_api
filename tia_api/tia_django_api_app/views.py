from django.shortcuts import render
from rest_framework import generics
from .serializers import DepartmentSerializer, ProductSerializer, OrderSerializer, Order_ProductSerializer, IndicatorsSerializer, Profit_By_HourSerializer, Dep_Pro_ProfitSerializer
from .models import Department, Product, Order, Order_Product, Indicators, Profit_By_Hour, Dep_Pro_Profit
from django.http import JsonResponse
from django.db.models import Sum
import json

# Create your views here.
class ListDepartment(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DetailDepartment(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ListOrder(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class DetailOrder(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ListOrder_Product(generics.ListCreateAPIView):
    queryset = Order_Product.objects.all()
    serializer_class = Order_ProductSerializer

class DetailOrder_Product(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order_Product.objects.all()
    serializer_class = Order_ProductSerializer

class ListIndicators(generics.ListCreateAPIView):
    queryset = Indicators.objects.all()
    serializer_class = IndicatorsSerializer

class DetailIndicators(generics.RetrieveUpdateDestroyAPIView):
    queryset = Indicators.objects.all()
    serializer_class = IndicatorsSerializer

class ListProfit_By_Hour(generics.ListCreateAPIView):
    queryset = Profit_By_Hour.objects.all()
    serializer_class = Profit_By_HourSerializer

class DetailProfit_By_Hour(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profit_By_Hour.objects.all()
    serializer_class = Profit_By_HourSerializer

class ListDep_Pro_Profit(generics.ListCreateAPIView):
    queryset = Dep_Pro_Profit.objects.all()
    serializer_class = Dep_Pro_ProfitSerializer

class DetailDep_Pro_Profit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dep_Pro_Profit.objects.all()
    serializer_class = Dep_Pro_ProfitSerializer


def get_top5_by_department(request):
    query = request.GET.get('department')
    print(query)
    top5 = Dep_Pro_Profit.objects.values('product','quantity').filter(department=query).order_by('-quantity')[:5]
    return JsonResponse({"data": top5[::1]})

def get_profit_by_product(request):
    query = request.GET.get('id')
    dep = Department.objects.get(id=query)
    data = dep.getProfitByProduct()
    return JsonResponse({"data": data[::1]})

def get_profit_by_department(request):
    data = Dep_Pro_Profit.objects.values('department').annotate(profit=Sum('profit')).order_by('-profit')
    return JsonResponse({"data": data[::1]})