from django.contrib import admin
from .models import Vendor, PurchaseOrder, Product, Category, ProductType, Priority, Responsible

admin.site.register(Vendor)
admin.site.register(PurchaseOrder)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductType)
admin.site.register(Priority)
admin.site.register(Responsible)
