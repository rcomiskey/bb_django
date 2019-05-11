from django.db import models

class MerchantCategory(models.Model):
    category = models.CharField(max_length=500, default='')

    def __str__(self):
            return self.category

class Merchant(models.Model):
    merchant_id = models.CharField(max_length=500, default='')
    name = models.CharField(max_length=500, default='')
    category = models.ManyToManyField(MerchantCategory)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    
    def __str__(self):
        return self.name 
        
class PromoType(models.Model):
    name = models.CharField(max_length=500, default='')
    
    def __str__(self):
        return self.name 
        
        
class Promotion(models.Model):
    promo_id = models.CharField(max_length=500, default='')
    merchant = models.ForeignKey('Merchant', on_delete=models.CASCADE)
    title = models.CharField(max_length=500, default='')
    description = models.CharField(max_length=500, default='')
    promo_type = models.ForeignKey('PromoType', on_delete=models.CASCADE) 
    start_date = models.CharField(max_length=500, default='')
    end_date = models.CharField(max_length=500, default='')
    deeplink = models.CharField(max_length=500, default='')
    category = models.ForeignKey('MerchantCategory', default='', null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
	

    
    