from django.shortcuts import render
from app.models import Pizza

# Create your views here.
def menu(request):

    pizzas = Pizza.objects.all()
    context ={
        'pizzas':pizzas
    }
    return render(request, 'base.html', context)