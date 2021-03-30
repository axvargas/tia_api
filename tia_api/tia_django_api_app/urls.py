from django.urls import path
from .views import ListDepartment, DetailDepartment, ListProduct, DetailProduct, ListOrder, DetailOrder, ListOrder_Product, DetailOrder_Product, ListIndicators, DetailIndicators, ListProfit_By_Hour, DetailProfit_By_Hour, get_top5_by_department, get_profit_by_product, ListDep_Pro_Profit, DetailDep_Pro_Profit, get_profit_by_department
urlpatterns = [
    path('departments', ListDepartment.as_view(), name= 'departments'),
    path('departments/<int:pk>/', DetailDepartment.as_view(), name='singledepartment'),

    path('products', ListProduct.as_view(), name= 'products'),
    path('products/<int:pk>/', DetailProduct.as_view(), name='singleproduct'),

    path('orders', ListOrder.as_view(), name= 'orders'),
    path('orders/<int:pk>/', DetailOrder.as_view(), name='singleorder'),

    path('order_product', ListOrder_Product.as_view(), name= 'order_product'),
    path('order_product/<int:pk>/', DetailOrder_Product.as_view(), name='singleorder_product'),

    path('indicators', ListIndicators.as_view(), name= 'indicators'),
    path('indicators/<int:pk>/', DetailIndicators.as_view(), name='single_indicators'),

    path('profit_by_hour', ListProfit_By_Hour.as_view(), name= 'profit_by_hour'),
    path('profit_by_hour/<int:pk>/', DetailProfit_By_Hour.as_view(), name='single_profit_by_hour'),

    path('department_product_profit', ListDep_Pro_Profit.as_view(), name= 'department_product_profit'),
    path('department_product_profit/<int:pk>/', DetailDep_Pro_Profit.as_view(), name='single_department_product_profit'),

    path('departments/get_top5', get_top5_by_department, name='department_product_profit'),
    path('departments/getProfitByProduct/', get_profit_by_product, name='get_profit_by_product'),
    path('departments/get_profit_by_department/', get_profit_by_department, name='get_profit_by_department'),
]
