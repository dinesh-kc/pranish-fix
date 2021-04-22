from django.shortcuts import render

# Create your views here.
def viewSales_Cash(request):
    return render(request, 'ViewSales_Cash.html')