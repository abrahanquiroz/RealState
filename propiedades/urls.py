from django.urls import path
from django.shortcuts import redirect
from rest_framework.routers import DefaultRouter
from .views import RealStateViewSet

router = DefaultRouter()
router.register(r"real_state", RealStateViewSet, basename="real_state")

urlpatterns = router.urls
