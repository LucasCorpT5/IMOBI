from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("senha")
        
        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0:
            return redirect('/auth/cadastro')

        return HttpResponse(f"{username}:{email}:{password}")



def login(request):
    return HttpResponse("Logar")
