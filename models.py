from django.db import models

# Create your models here.
class Product(models.Model):
    pname = models.CharField(max_length=20)
    price = models.FloatField(default=30)
    qty = models.IntegerField(default=10)

    class Meta:
        db_table  = "Product"