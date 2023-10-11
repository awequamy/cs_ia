
from .models import Category, Product


def get_categories(request):
    categories = Category.objects.filter(parent__isnull=True)
    shop = Category.objects.get(slug='shop')
    rent = Category.objects.get(slug='rent')
    return {'categories': categories, 'shop': shop, 'rent': rent}
