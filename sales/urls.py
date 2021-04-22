
from django.urls import path,include

from .views import *

urlpatterns = [
    path('sale_medicine', SellMedicine.as_view(),name='sell_medicine'),
    path('multiple_sell', MultipleSell,name='multiple_sell'),

    path('sale_medicine_report', SellMedicineReport.as_view(),name='sell_medicine_report'),
        # path('automate_file', AutomateFile,name='automate_file'),
]
