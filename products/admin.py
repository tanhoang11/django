from django.contrib import admin
from .models import Product
# Register your models here.admin.site.register(Product)
# class ProductsAdmin(admin.ModelAdmin):
#     list = '__all__'
    
admin.site.register(Product )
