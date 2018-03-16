from django.db import models

class MerchantCategory(models.Model):
    category = models.CharField(max_length=500, default='')

    def __str__(self):
            return self.category

class Merchant(models.Model):
    name = models.CharField(max_length=500, default='')
    image = models.ImageField(upload_to="images", blank=True, null=True)
    
    def __str__(self):
        return self.name 
        

class Promotion(models.Model):
    merchant = models.ForeignKey('Merchant', on_delete=models.CASCADE)
    title = models.CharField(max_length=500, default='')
    description = models.CharField(max_length=500, default='')
    promo_type = models.CharField(max_length=500, default='')
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    deeplink = models.CharField(max_length=500, default='')
    category = models.ForeignKey('MerchantCategory', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.promo_type
	

    
    