from django.shortcuts import render


# Create your views here.
def teste(request):
    return render(request, 'teste.html')

def login(request):
    return render(request, 'login.html')

def area_de_agendamento(request):
    return render(request, 'area_de_agendamento.html')

def home(request):
    return render(request, 'home.html')

def servicos(request):
    return render(request, 'servicos.html')

def farmacia(request):
    return render(request, 'farmacia.html')

def cadastro(request):
    return render(request, 'cadastro.html')
