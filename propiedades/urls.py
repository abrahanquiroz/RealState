from django.urls import path
from django.shortcuts import redirect
from rest_framework.routers import DefaultRouter
from .views import (
    RealStateViewSet,
    list_propiedades,
    create_propiedades,
    edit_propiedades,
    # delete_propiedades,  # Si activas la función de eliminar
)

# Función para redirigir la raíz ("/") a la lista de propiedades
def home_redirect(request):
    return redirect("list_propiedades")

# Enrutador para las API ViewSets de RealState
router = DefaultRouter()
router.register(r"real_state", RealStateViewSet, basename="real_state")

# URLs del enrutador + las URLs de las vistas personalizadas
urlpatterns = [
    # Redirección para la raíz de la aplicación
    path("", home_redirect),  # Redirige "/" a la lista de propiedades
    path("realstate/list", list_propiedades, name="list_propiedades"),
    path("realstate/create", create_propiedades, name="create_propiedades"),
    path("realstate/edit/<int:pk>", edit_propiedades, name="edit_propiedades"),
    # path("realstate/delete/<int:pk>", delete_propiedades, name="delete_propiedades"),  # Si necesitas eliminar
]

# Añadir las rutas de la API en un subdirectorio separado, por ejemplo, "api/"
urlpatterns += router.urls
