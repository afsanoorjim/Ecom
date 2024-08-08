from django.db import models

# Create your models here.
class Product(models.Model):
    IN_STOCK = 'In Stock'
    OUT_STOCK = 'Out of Stock'

    PRODUCT_STATUS = {
        IN_STOCK: 'In Stock',
        OUT_STOCK: 'Out of Stock'
    }

    product_name = models.CharField(max_length=500)
    product_image = models.ImageField(upload_to='images', default=None)
    product_overview = models. CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.IntegerField(default=0)
    product_status = models.CharField(max_length=50, choices=PRODUCT_STATUS, default=IN_STOCK)
    

    def __str__(self):
        return self.product_name