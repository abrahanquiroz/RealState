from django.urls import path
from .views import (
    list_properties,
    create_property,
    edit_property,
    home,
)

urlpatterns = [
    path('', home, name='home'),
    path("realstate/list", list_properties, name="list_properties"),
    path("realstate/create", create_property, name="create_property"),
    path("realstate/edit/<int:pk>", edit_property, name="edit_property"),
]
