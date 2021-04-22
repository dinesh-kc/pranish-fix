from django.shortcuts import render, redirect
from .models import Medicine
from django.http import HttpResponse
from .filters import OrderFilter
from automateFile.views import automateFile
# Create your views here.



def medicine_manage(request):
    if request.method == 'POST':
            data = request.POST
            med_name = data['med_name']
            price = data['price']
            selling_price = data['selling_price']
            supplier = data['supplier']
            bought_date = data['bought_date']
            expiry_date = data['expiry_date']
            time_table = data['time_table']
            quantity = data['quantity']

            obj = Medicine.objects.create(med_name = med_name, price=price,selling_price=selling_price,supplier=supplier,bought_date=bought_date,expiry_date=expiry_date,time_table=time_table, quantity=quantity)
            if obj:
                return redirect('/manage_medicine')
            return HttpResponse('Medicine is not added.')
    else:
            medicines = Medicine.objects.all()
            context= {
                'medicines':medicines,
            }
            
            return render(request, 'manage_medicine.html',context)
    


    return render(request, 'manage_medicine.html')

def medicine_update(request, id):
    medicine = Medicine.objects.get(id=id)
    if request.method == 'POST':
        medicine.med_name = request.POST['med_name']
        medicine.price = request.POST['price']
        medicine.selling_price = request.POST['selling_price']
        medicine.expiry_date = request.POST['expiry_date']
        medicine.supplier = request.POST['supplier']
        medicine.bought_date = request.POST['bought_date']
        medicine.time_table = request.POST['time_table']
        medicine.quantity = request.POST['quantity']
        medicine.save()
        return redirect('/manage_medicine')
    context={
        'medicine': medicine
    }
    return render(request, 'medicine_update.html', context)

def medicine_delete(request, id):
    medicine = Medicine.objects.get(id=id)
    if request.method == 'POST':
        medicine.delete()
        return redirect('/manage_medicine')

    context={
        'medicine': medicine
    }


    return render(request, 'medicine_delete.html', context)

