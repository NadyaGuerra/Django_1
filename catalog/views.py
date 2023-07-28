from django.shortcuts import render
from django.urls import reverse_lazy


from catalog.models import Product
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView


# def home(request):
#     product_list=Product.objects.all()
#     context = {
#         'object_list':product_list,
#         'title': 'Каталог'
#     }
#
#     return render(request, 'catalog/home_list.html', context)

class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home_list.html'
    success_url = reverse_lazy('home_list')


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


# def product(request):
#     product_list = Product.objects.all()
#     context = {
#         'object_list': product_list,
#         'title': 'Товары'
#     }
#     return render(request, 'catalog/home_list.html', context)
# class ProductListView(ListView):
#     model = Product
#     template_name = 'catalog/home_list.html'




# class CardDetailView(DetailView):
#     model = Product

class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'price', 'category', 'image')
    success_url = reverse_lazy('product_details')

class ProductUpdateView(UpdateView):
    model = Product
    fields=('name','description','preview','price')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products_list')