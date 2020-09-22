from django.urls import path, include, re_path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('documento', views.DocumentViewSet, basename="processador-palavras")
router.register('vocabulario-default', views.SequenceDefaultViewSet, basename="vocabulario-default")
router.register('vocabulario-grupo', views.Sequence2GramViewSet, basename="vocabulario-grupo")
