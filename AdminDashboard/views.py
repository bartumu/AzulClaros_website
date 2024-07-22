from django.shortcuts import render

# Create your views here.
def cliDashboard(request):
    return render(request,'BackEnd/home.html')
