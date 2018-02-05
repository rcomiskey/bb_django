from django.db import models

class Product(models.Model):
    aw_deep_link = models.CharField(max_length=500, default='')
    product_name = models.CharField(max_length=500, default='')
    aw_image_url = models.CharField(max_length=500, default='')
    # search_price = models.DecimalField(max_digits=6, decimal_places=2)
    merchant_name = models.CharField(max_length=500, default='')
    # display_price = models.DecimalField(max_digits=6, decimal_places=2)
    brand_name = models.CharField(max_length=500, default='')
    colour = models.CharField(max_length=500, default='')
    # rrp_price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.product_name
