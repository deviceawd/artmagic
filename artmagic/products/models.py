from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=255, unique=True)
    image_category = models.ImageField(upload_to='media/category', blank=True, null=True)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    image_product = models.ImageField(upload_to='media/product', blank=True, null=True)
    rate = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    manufacturer = models.CharField(max_length=255)
    article_no = models.CharField(max_length=255)
    availability = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )

    def __str__(self):
        return self.title
