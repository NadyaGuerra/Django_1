from django.db import models
from datetime import datetime
# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=100,verbose_name='наиминование')
    description=models.TextField(verbose_name='описание',blank=True,null=True)
    preview=models.ImageField(upload_to='products/', verbose_name='изображение',blank=True,null=True)
    category=models.ForeignKey('category', on_delete=models.SET_NULL,null=True,blank=True,verbose_name='категория')
    price=models.DecimalField(decimal_places=3,max_digits=10,verbose_name='цена')
    created_data=models.DateTimeField(auto_now_add=True,verbose_name='дата создания',blank=False,null=False)
    last_change=models.DateTimeField(auto_now=True,verbose_name='последние изменения',blank=False,null=False)


    def __str__(self):
        return f'{self.name}  {self.price}  категория:{self.category}'


    class Meta:
        verbose_name='Продукт'
        verbose_name_plural='Продукты'
        ordering=('name',)
class Category(models.Model):
    name=models.CharField(max_length=100,verbose_name='наименование')
    description=models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering=('name',)

