from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms  import PersonForm
from .models import Person

# Create your views here.
def teste(request):
    return render(request, 'teste.html')

def login(request):
    return render(request, 'login.html')

def agenda(request):
    return render(request, 'agenda.html')

def home(request):
    return render(request, 'home.html')

def servicos(request):
    return render(request, 'servicos.html')

def farmacia(request):
    return render(request, 'farmacia.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def pet(request):
    return render(request, 'pet.html')
def name(request):
    return render(request, 'name.html')

def serv(request):
    return render(request, 'serv.html')
def serv2(request):
    return render(request, 'serv2.html')

def agenda2(request):
    return render(request, 'agenda2.html')



def person_create(request):
    person_form = PersonForm(request.POST or
                             None,
                             request.FILES or
                             None)
    if person_form.is_valid():
        person = person_form.save(commit=False)
        person.save()
    return render(request, 'person_create.html',
                  {'person_form':person_form})

def person_read(request):
    persons = Person.objects.all()
    return render(request, 'person_read.html',
                  {'persons':persons})

def person_update(request, id):
    person = get_object_or_404(Person, pk=id)
    person_form = PersonForm(request.POST or
                             None,
                             request.FILES or
                             None,
                             instance=person)
    if person_form.is_valid():
        person = person_form.save(commit=False)
        person.save()

    return render(request,
                  'person_create.html',
                  {"person_form":person_form})

def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    person.delete()
    return redirect("read_person")