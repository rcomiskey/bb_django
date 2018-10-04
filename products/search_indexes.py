from haystack import indexes
from .models import Product

    class ProductIndex(indexes.SearchIndex, indexes.Indexable):
        text = indexes.CharField(document=True, use_template=True, template_name="templates/search.txt")
        product_name = indexes.CharField(model_attr='product_name')
        authors = indexes.CharField()
        def get_model(self):
            return Product
        def prepare_category(self, obj):
            return [ category.name for a in obj.category.all()]
        def index_queryset(self, using=None):
            return self.get_model().objects.all()