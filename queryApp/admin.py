from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from queryApp.models import *


@admin.register(MSE_CUSTOMERS)
class MSE_CUSTOMERS_ADMIN(admin.ModelAdmin):
    list_display = [f.name for f in MSE_CUSTOMERS._meta.fields]

@admin.register(MSE_MANUFACTURERS)
class MSE_MANUFACTURERS_ADMIN(ImportExportModelAdmin):
    pass
    list_display = [f.name for f in MSE_MANUFACTURERS._meta.fields]

