from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from propiedades.models import RealState


def list_properties(request):
    properties = RealState.objects.all().order_by("-id")
    return render(request, "list_properties.html", {"properties": properties})


def create_property(request):
    # if request.method == "POST":
    #     name = request.POST.get("name")
    #     address = request.POST.get("address")
    #     country = request.POST.get("country")
    #     city = request.POST.get("city")
    #     postal_code = request.POST.get("postal_code")
    #     type = request.POST.get("type")
    #     area = request.POST.get("area")

    #     if not all([name, address, country, city, postal_code, type, area]):
    #         return HttpResponseBadRequest("Faltan campos obligatorios")

    #     propiedades = RealState(
    #         name=name,
    #         address=address,
    #         country=country,
    #         city=city,
    #         postal_code=postal_code,
    #         type=type,
    #         area=area,
    #     )
    #     propiedades.save()

    #     return redirect("/realstate/list")

    return render(
        request,
        "create_property.html",
        {"REAL_STATE_TYPE": RealState.REAL_STATE_TYPE},
    )


def edit_property(request, pk):
    property = RealState.objects.get(id=pk)

    return render(
        request,
        "edit_property.html",
        {"property": property, "REAL_STATE_TYPE": RealState.REAL_STATE_TYPE},
    )
