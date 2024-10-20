from django.shortcuts import render, get_object_or_404
from django.http import request, response, HttpRequest, HttpResponse
from Spese.models import Tipologia, Destinazione, Movimento
from Spese.forms import AddTipologia, AddDestinazione, AddMovimento

from django.shortcuts import render
from .models import Movimento

def home(request):
    movimenti = Movimento.objects.all()
    return render(request, 'Spese/Home.html', {'movimenti': movimenti})

def lista_movimenti(request):
    movimento = Movimento.objects.all()
    context = {
        'movimento' : movimento
    }
    return render(request, 'Spese/Lista_Movimenti.html', context)

def lista_tipologia(request):
    tipologia = Tipologia.objects.all()
    context = {
        'tipologia' : tipologia,
    }
    return render(request, 'Spese/Lista_Tipologia.html', context)

def lista_destinazione(request):
    destinazione = Destinazione.objects.all()
    context = {
        'destinazione' : destinazione,
    }
    return render(request, 'Spese/Lista_Destinazione.html', context)

def add_tipologia(request):
    if request.method == 'POST':
        form = AddTipologia(request.POST)
        if form.is_valid():
            form.save()
    form = AddTipologia()
    context = {
        'form' : form,
    }
    return render(request, 'Spese/Add_Tipologia.html', context)

def add_destinazione(request):
    if request.method == 'POST':
        form = AddDestinazione(request.POST)
        if form.is_valid():
            form.save()
    form = AddDestinazione()
    context = {
        'form' : form,
    }
    return render(request, 'Spese/Add_Destinazione.html', context)

def add_movimento(request):
    if request.method == 'POST':
        form = AddMovimento(request.POST)
        if form.is_valid():
            form.save()
    form = AddMovimento()
    context = {
        'form' : form,
    }
    return render(request, 'Spese/Add_Movimento.html', context)

def dettaglio_movimento(request, movimento_id):
    movimento = get_object_or_404(Movimento, id=movimento_id)
    return render(request, 'Spese/Dettaglio_Movimento.html', {'movimento': movimento})