from django import forms 

from sales.models import MedicineTransaction

class MedicineTransactionForm(forms.ModelForm):
    class Meta: 
        model = MedicineTransaction
        fields = '__all__'