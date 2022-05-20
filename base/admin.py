from django.contrib import admin
from django.contrib.auth.models import User
from import_export import resources

from import_export import resources
from import_export.admin import ExportMixin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin

from base.models import Apparel, Footwear, Product

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

class FootwearRessource(resources.ModelResource):
    class Meta:
        model = Footwear
        fields = ('id','gender','masterCategory','subCategory','articleType','baseColor','season','year','usage','productDisplayName','price','link','stock38','stock39','stock40','stock41','stock42','stock43','stock44','stock45')

class FootwearAdmin(ImportExportModelAdmin,ExportMixin, admin.ModelAdmin):
    resource_class = FootwearRessource
    # Other admin definition here
    list_display = ('id','gender','masterCategory','subCategory','articleType','baseColor','season','year','usage','productDisplayName','price','link','stock38','stock39','stock40','stock41','stock42','stock43','stock44','stock45')
    # list_filter = ('created_at',)
    resource_class = FootwearRessource
    pass

class ApparelRessource(resources.ModelResource):
    class Meta:
        model = Apparel
        fields = ('id','gender','masterCategory','subCategory','articleType','baseColor','season','year','usage','productDisplayName','price','link','stocks','stockm','stockl','stockxl','stockxxl')

class ApparelAdmin(ImportExportModelAdmin,ExportMixin, admin.ModelAdmin):
    resource_class = ApparelRessource
    # Other admin definition here
    list_display = ('id','gender','masterCategory','subCategory','articleType','baseColor','season','year','usage','productDisplayName','price','link','stocks','stockm','stockl','stockxl','stockxxl')
    # list_filter = ('created_at',)
    resource_class = ApparelRessource
    pass

class ProductRessource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('id','gender','masterCategory','subCategory','articleType','baseColor','season','year','usage','productDisplayName','price','link')

class ProductAdmin(ImportExportModelAdmin,ExportMixin, admin.ModelAdmin):
    resource_class = ProductRessource
    # Other admin definition here
    list_display = ('id','gender','masterCategory','subCategory','articleType','baseColor','season','year','usage','productDisplayName','price','link')
    # list_filter = ('created_at',)
    resource_class = ProductRessource
    pass





admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Footwear, FootwearAdmin)  
admin.site.register(Apparel, ApparelAdmin) 
admin.site.register(Product, ProductAdmin)
