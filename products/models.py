from django.db import models
from mptt.models import MPTTModel, TreeForeignKey, TreeManager
import re
from django.db.models import Q


class Category(MPTTModel):
    regex = models.CharField(max_length=100, blank=True)
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

class Product(models.Model):
    aw_deep_link = models.CharField(max_length=500, default='')
    product_name = models.CharField(max_length=500, default='')
    aw_image_url = models.CharField(max_length=500, default='')
    search_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    merchant_name = models.CharField(max_length=500, default='')
    display_price = models.CharField(max_length=500, default='')
    brand_name = models.ForeignKey('Brand', on_delete=models.CASCADE)
    size = models.CharField(max_length=500, default='')
    colour = models.CharField(max_length=500, default='')
    rrp_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, default='')
    category = TreeForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, default='')
    aw_product_id = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.product_name
