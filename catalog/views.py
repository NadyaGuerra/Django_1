
from django.shortcuts import render
from catalog.models import Product





def home(request):
    context = {
        'title': 'Каталог'
    }

    return render(request, 'catalog/home.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')

    return render(request, 'catalog/contacts.html', context)


def product(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Продукты'
    }
    return render(request, 'catalog/product.html', context)
