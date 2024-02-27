from django.contrib import admin
from .models import Category, Product
from django.utils.safestring import mark_safe

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    serch_fields = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'image', 'description', 'created', 'updated')
    serch_fields = ('name',)
    list_filter = ('category',)

    def image(self, obj):
        return mark_safe('<img src="{}" style="width:100px height:auto;">'.format(obj.img.url))

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
