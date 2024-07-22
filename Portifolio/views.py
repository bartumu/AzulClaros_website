from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def index(request):
    is_logged = False
    if request.user.is_authenticated:
        is_logged = True

    context = {
        'is_logged':is_logged
    }
    return render(request,'Portifolio/index.html', context)
def sobre(request):
    return render(request,'Portifolio/SobreNos.html')