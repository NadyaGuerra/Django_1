from django.urls import path
from catalog.views import contacts, home, product,card

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', home, name='home'),
    path('<int:pk>/card/',card, name='card'),
    path('product/', product, name='product')
]

