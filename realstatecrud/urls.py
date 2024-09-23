from django.urls import path
from django.shortcuts import redirect
from .views import (
    list_properties,
    create_property,
    edit_property,
)


def home_redirect(request):
    return redirect("realstate/list")


urlpatterns = [
    path("", home_redirect),
    path("realstate/list", list_properties, name="list_properties"),
    path("realstate/create", create_property, name="create_property"),
    path("realstate/edit/<int:pk>", edit_property, name="edit_property"),
]
