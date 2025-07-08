from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'


class Product(models.Model):
    categories = models.ManyToManyField(Category)
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        db_table = 'product'


class ProductLog(models.Model):
    ACTION_CHOICES = (
        ('create', 'Created'),
        ('update', 'Updated'),
        ('delete', 'Deleted'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True,blank=True)
    action = models.CharField(choices=ACTION_CHOICES, max_length=10)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'product_log'
