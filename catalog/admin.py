from django.contrib import admin

# Register your models here.

from catalog.models import Category,Product,Version
# admin.site.register(Category)
# admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =( 'name',)
    list_filter = ('name',)

@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','price','category',)
    list_filter = ('category',)
    search_fields = ('name','description')

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ['product','version_number','version_name','is_active','description']