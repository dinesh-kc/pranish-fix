
from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render
from manage_medicines.views import medicine_manage, medicine_update,medicine_delete
from manageSaes_cash.views import sales_cash
from manageSaes_credit.views import sales_credit
from viewSales_Cash.views import viewSales_Cash
from viewSales_Credit.views import viewSales_Credit
from orderMedicine.views import orderMedicine
from automateFile.views import automateFile
from viewUsers.views import viewUsers

from django.contrib.auth import views as auth_views #password change


from django.contrib.auth.decorators import login_required
from .views import *

@login_required
def dashboard(request):
    return render(request, 'base.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard),
    path('accounts/',include('django.contrib.auth.urls')),
    path('sales/',include('sales.urls')),
    path('home', dashboard),
    path("register/", register, name="register"),
    path("change_password/", change_password, name="change_password"),
    path("register_view/", register_view, name="register_view"),
    
    # path("logout/", logout, name="logout"),
    path('manage_medicine', medicine_manage),
    path('sales_cash', sales_cash),
    path('sales_credit', sales_credit),
    path('viewSales_Cash', viewSales_Cash),
    path('viewSales_Credit', viewSales_Credit),
    path('orderMedicine', orderMedicine),
    path('automateFile', automateFile),
    # path('viewUsers', viewUsers),
    path('medicine_update/<int:id>', medicine_update),
    path('medicine_delete/<int:id>', medicine_delete),



    # url for passworf reset 
    # path('accounts/', include('django.contrib.auth.urls')),
    path("password_reset", password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),  

]
