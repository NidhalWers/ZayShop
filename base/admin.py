from django.contrib import admin
from django.contrib.auth.models import User
from import_export import resources

from import_export import resources
from import_export.admin import ExportMixin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin

from base.models import Product

# Register your models here.
class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('id','username','first_name', 'last_name', 'email')

# class UserAdmin(ExportMixin, UserAdmin):
#     resource_class = UserResource
#     pass

class UserAdmin(ImportExportModelAdmin):
    list_display = ('id','username','first_name', 'last_name', 'email')
    # list_filter = ('created_at',)
    resource_class = UserResource
    pass

class ProductRessource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('id','name','description','price')

class ProductAdmin(ImportExportModelAdmin,ExportMixin, admin.ModelAdmin):
    resource_class = ProductRessource
    # Other admin definition here
    list_display = ('id','name','description','price','image')
    # list_filter = ('created_at',)
    resource_class = ProductRessource
    pass



admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)  
