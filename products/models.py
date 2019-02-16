from django.db import models
from mptt.models import MPTTModel, TreeForeignKey, TreeManager
from django.contrib.postgres.search import SearchVectorField, SearchVector
from django.contrib.postgres.indexes import GinIndex
import re
from django.db.models import Q


class Category(MPTTModel):
    regex = models.CharField(max_length=100, blank=True, default='^dontmatch$')
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True,
                            on_delete=models.CASCADE)
    slug = models.SlugField()

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = (('parent', 'slug',))
        verbose_name_plural = 'categories'

    def get_slug_list(self):
        try:
            ancestors = self.get_ancestors(include_self=True)
        except:
            ancestors = []
        else:
            ancestors = [i.slug for i in ancestors]
        slugs = []
        for i in range(len(ancestors)):
            slugs.append('/'.join(ancestors[:i + 1]))
        return slugs

    def get_all_products(self):
        # To display all items from all subcategories
        return Product.objects.filter(category__in=self.get_descendants(include_self=True))

    def __str__(self):
        return self.name


class Brand(models.Model):
    brand_name = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.brand_name


class Merchant(models.Model):
    merchant_name = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.merchant_name


class Product(models.Model):
    aw_deep_link = models.CharField(max_length=500, default='')
    product_name = models.CharField(max_length=500, default='')
    aw_image_url = models.CharField(max_length=500, default='')
    search_price = models.CharField(max_length=500, default='')
    merchant_name = models.ForeignKey('Merchant', on_delete=models.CASCADE)
    brand_name = models.ForeignKey('Brand', on_delete=models.CASCADE)
    size = models.CharField(max_length=500, default='')
    colour = models.CharField(max_length=500, default='')
    rrp_price = models.CharField(max_length=500, default='')
    category = TreeForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=5000, default='')
    aw_product_id = models.CharField(max_length=500, default='', unique=True)
    currency = models.CharField(max_length=500, default='')
    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [
            GinIndex(fields=['search_vector'])
        ]

    def __str__(self):
        return self.product_name
