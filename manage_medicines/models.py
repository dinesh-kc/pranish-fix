from django.db import models

# Create your models here.
class Medicine(models.Model):
    med_name = models.CharField(max_length = 30)
    price = models.CharField(max_length = 30)
    selling_price = models.CharField(max_length = 30)
    supplier = models.CharField(max_length = 30)
    bought_date = models.CharField(max_length = 30)
    expiry_date = models.CharField(max_length = 30)
    time_table = models.CharField(max_length = 30)
    quantity = models.IntegerField()

    def __str__(self):
        return self.med_name

    @property
    def total_amount(self):
        return self.selling_price
