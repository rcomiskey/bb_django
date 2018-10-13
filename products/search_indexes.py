from haystack import indexes
from products.models import Product


class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name="search/product_text.txt")
    product_name = indexes.CharField(model_attr='product_name')
    brand_name = indexes.CharField()

    def get_model(self):
        return Product

    def prepare_brand_name(self, obj):
        return [ brand_name.brand_name for a in obj.brand_name.all()]

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
