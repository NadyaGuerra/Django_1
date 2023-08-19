from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from django.forms import inlineformset_factory
from catalog.forms import ProductForm
from catalog.models import Product
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView
from catalog.models import Version
from catalog.forms import ProductForm,VersionForm
from catalog.services import get_cashed_categories
# def home(request):
#     product_list=Product.objects.all()
#     context = {
#         'object_list':product_list,
#         'title': 'Каталог'
#     }
#
#     return render(request, 'catalog/product_list.html', context)

class ProductListView(ListView):
    model = Product
    # template_name = 'catalog/product_list.html'
    # success_url = reverse_lazy('product_list')


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
#     return render(request, 'catalog/product_list.html', context)
# class ProductListView(ListView):
#     model = Product
#     template_name = 'catalog/product_list.html'




# class CardDetailView(DetailView):
#     model = Product

class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    # fields = ('name', 'description', 'price', 'category', 'image')
    success_url = reverse_lazy('product_list')

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
    #     if self.request.method == 'POST':
    #         context_data['formset'] = VersionFormset(self.request.POST)
    #     else:
    #         context_data['formset'] = VersionFormset()
    #     return context_data

    # def form_valid(self, form):
    #     formset = self.get_context_data()['formset']
    #     self.object = form.save()
    #     if formset.is_valid():
    #         formset.instance = self.object
    #         formset.save()
    #     return super().form_valid(form)

class ProductUpdateView(UpdateView):
    model = Product
    #fields=('name','description','preview','price')
    form_class = ProductForm
    success_url = reverse_lazy('product_list')

    def get_context_data(self, **kwargs):
        context_data=super().get_context_data()
        VersionFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('card', args=[self.kwargs.get('pk')])

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')


class VersionListView(ListView):
    model = Version

    def get_queryset(self, *args, **kwargs):

        product_pk = self.kwargs.get('pk')
        return Version.objects.filter(is_active=True, product_id=product_pk)

    def get_context_data(self, *args, object_list=None, **kwargs):

        product = Product.objects.get(pk=self.kwargs.get('pk'))
        context = super().get_context_data(*args, **kwargs)
        context['product_name'] = product.name
        context['pk'] = product.pk
        return context

def categories_list(request):
    catetegories=get_cashed_categories()
    context={'object_list': catetegories,}
    return render(request, 'catalog/categories.html',context)