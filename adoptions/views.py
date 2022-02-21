from django.shortcuts import render
from django.http import Http404

from .models import Pet

def home(request):
    pets = Pet.objects.all()
    context = {'pets': pets}
    return render(request, 'home.html', context)

def pet_details(request, pet_id):
    try:
        pet = Pet.objects.get(id = pet_id)
    except :
        return Http404('pet not found')
    
    context = {'pet': pet}
    return render(request, 'details.html', context)