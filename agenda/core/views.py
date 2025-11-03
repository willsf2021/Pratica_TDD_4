from django.shortcuts import render, redirect
from core.forms import LoginForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import AgendaForm
from .models import Agenda

def login(request):
    if request.user.id is not None:
        return redirect("home")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            auth_login(request, form.user)
            return redirect("home")
        context = {'acesso_negado': True}
        return render(request, 'login.html', {'form':form})
    return render(request, 'login.html', {'form':LoginForm()})

        
def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return render(request, 'logout.html')
    return redirect("home")


@login_required
def home(request):
    
    context = {}
    return render(request, 'index.html', context)


@login_required
def create_contact(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AgendaForm()
        return render(request, 'create_contact.html', {'form': form, 'titulo': "Adicionar um contato"})
    
    
@login_required
def list_contacts(request):
    contacts = Agenda.objects.all()
    return render(request, 'list_contacts.html', {'contacts': contacts, 'titulo': 'Listar contatos'})
    
    
@login_required
def detail_contact(request, pk):
    contact = Agenda.objects.filter(pk=pk)
    # nome = contact.nome_completo
    return render(request, 'detail_contact.html', {'contact':contact})