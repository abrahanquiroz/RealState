from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from propiedades.models import RealState

def home(request):
    return render(request, 'home.html')


def list_properties(request):
    return render(request, "list_properties.html",)


def create_property(request):
    return render(
        request,
        "create_property.html",
        {"REAL_STATE_TYPE": RealState.REAL_STATE_TYPE},
    )


def edit_property(request, pk):
    try:
        property = RealState.objects.get(pk=pk)
    except RealState.DoesNotExist:
        return HttpResponseBadRequest("Property not found")

    return render(
        request,
        "edit_property.html",
        {"property": property, "REAL_STATE_TYPE": RealState.REAL_STATE_TYPE},
    )
