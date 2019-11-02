from django.contrib import admin

# Register your models here.
from queryApp.models import MSE_CUSTOMERS


@admin.register(MSE_CUSTOMERS)
class MSE_CUSTOMERS_ADMIN(admin.ModelAdmin):
    list_display = [f.name for f in MSE_CUSTOMERS._meta.fields]