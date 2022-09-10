from django.shortcuts import render
from platos.models import Platos
from django.db.models import Q

# Serializador
from django.core import serializers as srr
from django.http import HttpResponse

def platos_list(request):

    #query = Q(pais__startswith='bra') | Q(edad__lt=17)
    #print("Query: {}".format(query))
    #data_context = Platos.objects.filter(query)

    data_context = Platos.objects.all()

    return render(request, 'platos/platos_list.html', context={'data': data_context})

def platos_search(request):
    query = request.GET.get('q', '')
    #print("query: {}".format(query))
    results = (
        Q(nombre__icontains=query)
    )
    print("resuts: {}".format(results))
    data_context = Platos.objects.filter(results).distinct()

    return render(request, 'platos/platos_search.html', context={'data': data_context, "query": query})


"""Serializador"""


def ListPlatosSerializer(request):
    #lista = serializers.serialize('json', Owner.objects.all())
    lista = srr.serialize('json', Platos.objects.all(), fields=['nombre', 'procedencia'])
    return HttpResponse(lista, content_type='application/json')




