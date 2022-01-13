from django.http import HttpResponse 
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from  .models import Imovei

# Create your views here.
@login_required(login_url="/auth/login")
def home(request):
    imoveis = Imovei.objects.all()
    return render(request, 'home.html', {'imoveis': imoveis})