from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

class ProductType(models.Model):
    name = models.CharField(max_length=255)

class Priority(models.Model):
    name = models.CharField(max_length=255)

class Responsible(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, default='OdooBot')

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    is_a_company = models.BooleanField(default=False)
    related_company = models.CharField(max_length=255)
    address_type = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

class PurchaseOrder(models.Model):
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    order_reference = models.CharField(max_length=255)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    purchase_representative = models.ForeignKey(Responsible, on_delete=models.CASCADE)
    order_deadline = models.DateTimeField()
    activities = models.TextField()
    source_document = models.TextField()
    total = models.FloatField()
    status = models.CharField(max_length=255)

class Product(models.Model):
    favorite = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    internal_reference = models.CharField(max_length=255)
    responsible = models.ForeignKey(Responsible, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=255)
    sales_price = models.FloatField()
    cost = models.FloatField()
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    quantity_on_hand = models.IntegerField()
    forecasted_quantity = models.IntegerField()
    activity_exception_decoration = models.CharField(max_length=255)
