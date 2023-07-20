
from django.shortcuts import render
from catalog.models import Product





def home(request):
    product_list=Product.objects.all()
    context = {
        'object_list':product_list,
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
        'title': 'Товары'
    }
    return render(request, 'catalog/home.html', context)

def card(request,pk):
    context={
        'object_list': Product.objects.filter(pk=pk)
    }
    return render(request, 'catalog/card.html', context)
