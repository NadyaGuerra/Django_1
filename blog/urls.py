from django.urls import path,include
from blog.apps import BlogConfig

app_name = BlogConfig.name
from blog.views import BlogCreateView,BlogListView,BlogUpdateView,BlogDeleteView,BlogDetailView

urlpatterns = [

    path('create/', BlogCreateView.as_view(), name='create'),
    path('blog_list/',BlogListView.as_view(),name='list'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
]
#     path('blog_detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
#     path('blog_update/<int:pk>/', BlogUpdateView.as_view(), name='update_blog'),
#     path('blog_delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),
#     path('is_published/<int:pk>/', toggle_published, name='is_published')
#
# ]
