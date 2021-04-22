from django.db import models



from manage_medicines.models import Medicine

TRANSACTION_TYPE = (
    (1,'debit'),
    (2,'credit')
)

class MedicineTransaction(models.Model):
    # is_first_entry = models.BooleanField(default=False)

    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE)
    received_amount = models.IntegerField(default=0)
    medicine = models.ForeignKey(Medicine,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=5,null=True,blank=True)
    customer_name = models.CharField(max_length=255,null=True,blank=True)
    is_final_entry = models.BooleanField(default=False)

    @property
    def amount_to_pay(self):
        # print(self.medicine.selling_price)
        return int(self.medicine.selling_price) * int(self.quantity)
    @property
    def remaining_amount(self):
        total = int(self.medicine.selling_price) * int(self.quantity)
        remaining = total - int(self.received_amount)
        return remaining


      
   