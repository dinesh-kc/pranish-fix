from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from manage_medicines.models import Medicine
# Register your models here.

@admin.register(Medicine)
class MedicineAdmin(ImportExportModelAdmin):
    pass
# Register your models here.
