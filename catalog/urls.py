from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, VersionListView
from catalog.views import categories_list

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', cache_page(60)(ProductListView.as_view()), name='product_list'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='card'),
    path('product_details/', ProductCreateView.as_view(), name='create_product'),
    path('edit_product/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('versions/<int:pk>', VersionListView.as_view(), name='version'),
    path('categories/', categories_list, name='categories')
]
