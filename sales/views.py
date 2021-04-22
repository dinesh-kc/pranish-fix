from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView,TemplateView
from django.urls import reverse
from manage_medicines.models import Medicine



from sales.forms import *

class ShareData:
    TotalSells = []

    def __init__(self):
        pass

    def get(self):
        return self.TotalSells
    def set_total(self,tmp):
        self.TotalSells.append(tmp)


class SellMedicine(LoginRequiredMixin,FormView):
    template_name = 'sell/new_sell.html'
    form_class = MedicineTransactionForm
    TotalSells  = []
    # success_url = '/sales/sale_medicine_report'
    # def post(self)
    def reset_var(self):
        self.TotalSells = []

    def post(self, request, *args, **kwargs):
  
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            print(form.cleaned_data['is_first_entry'])
            if form.cleaned_data['is_first_entry']:
                # print("this is first entttry ")
                self.reset_var()
            print(self.TotalSells)

            return self.form_valid(form)
        else:
            return self.form_invalid(form)
 
    def form_valid(self, form):
        print("total sells")
        # print(self.request.session['TotalSells'])
        temp = {}
        
        try:
            print(self.request.session['TotalSells'])
            TotalMedicineSells = self.request.session['TotalSells']
        except:
            TotalMedicineSells = []

        obj = form.save(commit=False)
        mobj = Medicine.objects.get(id=obj.medicine.id)
        if obj.quantity > mobj.quantity:
            return render(self.request,self.template_name,{'form':form,'mquantity':mobj.quantity})
        temp = {
            'transaction_type':obj.transaction_type,
            'received_amount':obj.received_amount,
            'medicine_id':obj.medicine.id,
            'quantity':obj.quantity,
            'customer_name':obj.customer_name
        }
        TotalMedicineSells.append(temp)

        self.request.session['TotalSells'] = TotalMedicineSells
        if obj.is_final_entry:
            print(dict(self.request.session))
            medicines_orders = self.request.session['TotalSells']
            for medicine in medicines_orders:
                MedicineTransaction.objects.create(**medicine)
                mobj = Medicine.objects.get(id=medicine['medicine_id'])
                mobj.quantity -= medicine['quantity']
                mobj.save()

            del self.request.session['TotalSells'] 
            self.request.session.modified=True
            
            # self.reset_var()
            return redirect('sell_medicine_report')

            # print("this is final entry")
            # self.TotalSells = []
        # medicine_id = obj.medicine.id 
        # mobj = Medicine.objects.get(id=medicine_id)
        # mobj.quantity -= obj.quantity
        # mobj.save()
        # obj.save() 
        frm = MedicineTransactionForm()
        # print(TotalSells)
        return render(self.request,self.template_name,{'form':frm,'TotalSells':self.request.session['TotalSells']})

def MultipleSell(request):
    # print(dict(request.session))
    TotalSells =  request.session['TotalSells']
    # print(TotalSells)
    for medicine in TotalSells:
        MedicineTransaction.objects.create(**medicine)
        mobj = Medicine.objects.get(id=medicine['medicine_id'])
        mobj.quantity -= medicine['quantity']
        mobj.save()

    # del request.session['TotalSells']
    # request.session.modified = True

    del request.session['TotalSells']
    request.session.modified=True
    print(dict(request.session))
    # print(request.session['TotalSells'])
    return redirect('sell_medicine_report')




class SellMedicineReport(LoginRequiredMixin,TemplateView):
    template_name = 'sell/sell_item.html'

    def get_context_data(self, **kwargs):
        kwargs.setdefault('view', self)
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        kwargs['transactions'] = MedicineTransaction.objects.all()
        # print(kwargs['transactions'])
        return kwargs

# @login_required
# def AutomateFile(request):

