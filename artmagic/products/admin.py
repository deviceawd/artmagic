from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category, Product


class CategoryAdmin(MPTTModelAdmin):
    list_display = ["name", "parent", "tree_id", "level"]
    search_fields = ["name"]


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "rate",
        "price",
        "manufacturer",
        "article_no",
        "availability",
        "quantity",
        "category",
    ]
    list_filter = ["availability", "category"]
    search_fields = ["title", "manufacturer", "article_no"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
