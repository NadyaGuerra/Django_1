from django.conf import settings
from django.core.cache import cache

from catalog.models import Category


def get_cashed_categories():
    if settings.CACHE_ENABLED:
        key = 'categories'
        categories_list = cache.get(key)

        if categories_list is None:
            categories_list = Category.objects.all()
            cache.set(key, categories_list)


    else:
        categories_list = Category.objects.all()
    return categories_list
