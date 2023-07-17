from django.urls import path
from catalog.views import contacts, home, product

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', home, name='home'),
    path('product/', product, name='product')
]
