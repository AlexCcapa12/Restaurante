from django.shortcuts import render
from meseros.models import Meseros
from django.db.models import Q

def meseros_list(request):
    query = Q(procedencia__startswith='bra') & Q(edad__lt=22)
    print("Query: {}".format(query))
    data_context = Meseros.objects.filter(query)

    #data_context = Meseros.objects.all()

    return render(request, 'meseros/meseros_list.html', context={'data': data_context})
