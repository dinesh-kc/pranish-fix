from import_export import resources
from manage_medicines.models import Medicine

class MedicineResouce(resources.ModelResource):
    class meta:
        model = Medicine