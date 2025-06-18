from django.contrib import admin
from .models import BikeBrand, BikeModel, Accessory

@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'bike_model', 'price', 'in_stock']
    list_filter = ['bike_model', 'category']
    search_fields = ['name']

@admin.register(BikeModel)
class BikeModelAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'brand')
    list_filter = ('model_name','brand')
    search_fields = ('model_name', 'brand')



@admin.register(BikeBrand)
class BikeBrandAdmin(admin.ModelAdmin):
    list_display = ('name','id')
    search_fields = ('name','id')
