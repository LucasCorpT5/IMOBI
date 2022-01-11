from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("senha")

        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/auth/cadastro')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Usuario já existe')
            return redirect('/auth/cadastro')

        try:
            user = User.objects.create_user(username=username, email=email, password=password)

            if not "@" in email:
                messages.add_message(request, constants.ERROR, 'Email invalido')
                return redirect('/auth/cadastro')
            else:
                user.save()
                messages.add_message(request, constants.SUCCESS, 'Usuario criado com sucesso!')
                return redirect('/auth/login')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/auth/cadastro')


def login(request):
    if request.method == "GET":
        return render(request, 'logar.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('senha')

        usuario = auth.authenticate(username=username, password=password)

        if not usuario:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha invalidos')
            return redirect('/auth/login')
        else:
            auth.login(request, usuario)
            return redirect('/')
