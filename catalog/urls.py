from django.urls import path
from catalog.views import contacts, ProductListView,ProductDetailView,ProductCreateView,ProductUpdateView,ProductDeleteView,VersionListView

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(),name = 'card'),
    path('product_details/', ProductCreateView.as_view(), name='create_product'),
    path('edit_product/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('versions/<int:pk>', VersionListView.as_view(), name='version'),

]
