from django.urls import path
from catalog.views import contacts, HomeListView,ProductDetailView,ProductCreateView,ProductUpdateView,ProductDeleteView

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', HomeListView.as_view(), name='home_list'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(),name = 'card'),
    path('product_details/', ProductCreateView.as_view(), name='create_product'),
    path('edit_product/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),

]
