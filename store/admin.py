from django.contrib import admin
from .models import Product, Variation

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'varition_category', 'varition_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'varition_category', 'varition_value')

admin.site.register(Product,ProductAdmin)
admin.site.register(Variation)