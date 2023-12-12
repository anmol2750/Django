from django.db import models

class CartItem(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()