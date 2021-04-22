from django.db import models

# Create your models here.
class Order(models.Model):
    sender_mail = models.CharField(max_length = 30)
    ordered_medicine = models.CharField(max_length = 10000)
    supplier_name = models.CharField(max_length = 100)
    
