from django.shortcuts import render

# Create your views here.
def sales_credit(request):
    return render(request, 'sales_credit.html')