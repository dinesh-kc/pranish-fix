from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Order
from django.http import HttpResponse


# Create your views here.
def orderMedicine(request):
    if request.method == "POST":
        to = request.POST.get('toEmail')
        items = request.POST.get('orderItems')
        send_mail("Order Medicine",items,settings.EMAIL_HOST_USER, [to], fail_silently=False)
        # send_mail(
        #     # Subject 
        #     "Order Medicine",
        #     # Message
        #     items,
        #     #from email
        #     settings.EMAIL_HOST_USER
        #     #rec list
        #     [to]
        # )
        supplier = request.POST.get('supplier')
        return render(request,'orderMedicine.html')
    else:
        return render(request,'orderMedicine.html')


