from django.contrib import admin
from .models import product , offer


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(offer, OfferAdmin)
admin.site.register(product, ProductAdmin)