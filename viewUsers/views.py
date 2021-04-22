from django.shortcuts import render

# Create your views here.
def viewUsers(request):
    return render(request, 'viewUsers.html')