from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   list_display = ('title','user','price','color','stok')
   readonly_fields = ('slug',) # değer girilemez
   search_fields = ('title','user')


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
   list_display = ('title',)

   
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
   list_display = ('product',)
   search_fields = ('product',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
   list_display = ('product','user',"date_now")
   search_fields = ('product','user')

   
@admin.register(ShopBasket)
class ShopBasketAdmin(admin.ModelAdmin):
   list_display = ('product','user',"quanity", "total_price")
   search_fields = ('product','user')