from django.contrib import admin
from .models import Drinks
from .models import Product
from import_export.admin import ImportExportModelAdmin
from .resources import ProductResource

admin.site.register(Drinks)
admin.site.register(Product)

# @admin.register(Product)
# class YourModelAdmin(ImportExportModelAdmin):
#     resource_class = ProductResource