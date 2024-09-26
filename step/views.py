from django.shortcuts import get_object_or_404, render
from .models import Aziende, Competenze, Offerte, Offerte_competenze
from django.shortcuts import render, redirect, get_object_or_404




def step (request):
    Offertes = Offerte.objects.all()
    Azienda = Aziende.objects.all()

    return render(request, 'step/step.html' , {
        'Offertes':Offertes,
        'Azienda':Azienda,
    })


def offerta (request, id_offerta):
    offerta = get_object_or_404(Offerte, id_offerta=id_offerta)
    competenze = Offerte_competenze.objects.filter(id_offerta=offerta).select_related('id_competenza')

    return render(request, 'step/offerta.html' , {
        'offerta':offerta,
        'competenze': competenze,
        })
