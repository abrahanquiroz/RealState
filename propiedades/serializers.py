from rest_framework import serializers
from .models import RealState


class RealStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealState
        fields = "__all__"
