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
    ordering = ("id",)
