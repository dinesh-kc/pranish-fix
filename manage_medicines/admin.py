from django.contrib import admin
from .models import Medicine
from import_export.admin import ImportExportModelAdmin


# Register your models here.
admin.site.register(Medicine)
class viewAdmin(ImportExportModelAdmin):
    pass
