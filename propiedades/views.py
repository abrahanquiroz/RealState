from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from rest_framework import filters, viewsets
from rest_framework.permissions import AllowAny
from .models import RealState
from .serializers import RealStateSerializer


class RealStateViewSet(viewsets.ModelViewSet):
    queryset = RealState.objects.all()
    serializer_class = RealStateSerializer
    permission_classes = (AllowAny,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ("id", "name", "country", "city", "postal_code", "area")
    ordering = ('id',)



def list_propiedades(request):
    propiedades = RealState.objects.all().order_by("-id")
    return render(request, "list_propiedades.html", {"propiedades": propiedades})


def create_propiedades(request):
    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        country = request.POST.get("country")
        city = request.POST.get("city")
        postal_code = request.POST.get("postal_code")
        type = request.POST.get("type")
        area = request.POST.get("area")

        if not all([name, address, country, city, postal_code, type, area]):
            return HttpResponseBadRequest("Faltan campos obligatorios")

        propiedades = RealState(
            name=name,
            address=address,
            country=country,
            city=city,
            postal_code=postal_code,
            type=type,
            area=area,
        )
        propiedades.save()

        return redirect("/realstate/list")
    
    return render(request, "create_propiedades.html", {"REAL_STATE_TYPE": RealState.REAL_STATE_TYPE})


def edit_propiedades(request, pk):
    propiedad = RealState.objects.get(id=pk)

    return render(request, "edit_propiedades.html", {"propiedad": propiedad, "REAL_STATE_TYPE": RealState.REAL_STATE_TYPE})