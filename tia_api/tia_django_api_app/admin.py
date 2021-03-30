from django.contrib import admin
from .models import Department, Product, Order, Order_Product, Indicators, Profit_By_Hour, Dep_Pro_Profit
# Register your models here.

admin.site.register(Department)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Order_Product)
admin.site.register(Indicators)
admin.site.register(Profit_By_Hour)
admin.site.register(Dep_Pro_Profit)