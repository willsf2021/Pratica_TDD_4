from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from core.forms import LoginForm
from .forms import AgendaForm
from .models import Agenda


def login(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = LoginForm(request.POST or None)
    context = {'form': form}

    if request.method == "POST":
        if form.is_valid():
            auth_login(request, form.user)
            return redirect("home")
        context['acesso_negado'] = True

    return render(request, 'login.html', context)


def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return render(request, 'logout.html')
    return redirect("home")




@login_required
def home(request):
    return render(request, 'index.html')

@login_required
def create_contact(request):
    form = AgendaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('list_contacts')

    context = {'form': form, 'titulo': "Adicionar contato"}
    return render(request, 'create_contact.html', context)

@login_required
def list_contacts(request):
    contacts = Agenda.objects.all().order_by('nome_completo')
    context = {'contacts': contacts, 'titulo': 'Lista de contatos'}
    return render(request, 'list_contacts.html', context)


@login_required
def detail_contact(request, pk):
    contact = get_object_or_404(Agenda, pk=pk)
    context = {'contact': contact, 'titulo': contact.nome_completo}
    return render(request, 'detail_contact.html', context)


@login_required
def update_contact(request, pk):
    contact = get_object_or_404(Agenda, pk=pk)
    form = AgendaForm(request.POST or None, instance=contact)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('detail_contact', pk=contact.pk)

    context = {'form': form, 'titulo': f'Editar {contact.nome_completo}'}
    return render(request, 'update_contact.html', context)


@login_required
def delete_contact(request, pk):
    contact = get_object_or_404(Agenda, pk=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('list_contacts')

    context = {'contact': contact, 'titulo': f'Excluir {contact.nome_completo}'}
    return render(request, 'delete_contact.html', context)
