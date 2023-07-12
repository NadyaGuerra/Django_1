from django.urls import path
from catalog.views import contact, home

urlpatterns = [
    path('', contact, name='contact'),
    path('', home, name='home')
]