# Заполнение справочников товаров и категорий

from django.core.management import BaseCommand, call_command

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        call_command('loaddata', 'data_product.json')

