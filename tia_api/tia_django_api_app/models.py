from django.db import models
from django.db.models import Sum, F
# Create your models here.

class Department(models.Model):
    department = models.CharField(max_length=255)

    def __str__(self):
        return self.department

    def getTop5Products(self):
        return Order_Product.objects.filter(product__department=self.id).values('product__product_name').annotate(total_vendido=Sum('quantity')).order_by('-total_vendido')[0:5]

    def getProfitByProduct(self):
        return Order_Product.objects.filter(product__department=self.id).values('product__product_name', 'product__department__department').annotate(total_profit=Sum(F('quantity') * F('product__margin') * F('product__price'),output_field=models.FloatField())).order_by('-total_profit')
    class Meta:
        db_table = 'departments'
        indexes = [
            models.Index(fields=['department']),
        ]

class Product(models.Model):
    product_name = models.CharField(max_length=10000)
    department = models.ForeignKey(Department, related_name="products", on_delete=models.CASCADE)
    price = models.FloatField()
    margin = models.FloatField()

    def __str__(self):
        return self.product_name
    class Meta:
        db_table = 'products'
        indexes = [
            models.Index(fields=['department']),
        ]

class Order(models.Model):
    order_hour_of_day = models.IntegerField()
    products = models.ManyToManyField(Product, through="Order_Product")
    def __str__(self):
        return self.order_hour_of_day

    class Meta:
        db_table = 'orders'
        indexes = [
            models.Index(fields=['order_hour_of_day']),
        ]

class Order_Product(models.Model):
    order = models.ForeignKey(Order, related_name="order_products_order", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="order_products_product", on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return '{} {} {}'.format(self.order_id, self.product_id, self.quantity)
    
    def ganancia(self):
        return self.product.price * self.product.margin * self.quantity

    class Meta:
        db_table = 'order_product'
        indexes = [
            models.Index(fields=['order', 'product']),
        ]

class Indicators(models.Model):
    avg_tickets = models.FloatField()
    avg_margin = models.FloatField()
    avg_products_qty = models.FloatField()

    def __str__(self):
        return '{} {} {}'.format(self.avg_tickets, self.avg_margin, self.avg_products_qty)
    class Meta:
        db_table = 'indicators'

class Profit_By_Hour(models.Model):
    hour_of_day = models.FloatField()
    income = models.FloatField()
    profit = models.FloatField()

    def __str__(self):
        return '{} {} {}'.format(self.hour_of_day, self.income, self.profit)
    class Meta:
        db_table = 'profit_by_hour'
        indexes = [
            models.Index(fields=['hour_of_day']),
        ]

class Dep_Pro_Profit(models.Model):
    department = models.CharField(max_length=255)
    product = models.CharField(max_length=9999)
    profit = models.FloatField()
    quantity = models.IntegerField(default=None)

    def __str__(self):
        return '{} {} {} {}'.format(self.department, self.product, self.profit, self.quantity)
    class Meta:
        db_table = 'dep_pro_profit'
        indexes = [
            models.Index(fields=['department']),
        ]
        