from django.shortcuts import render

# Create your views here.

def sales_cash(request):
    return render(request, 'sales_Cash.html')