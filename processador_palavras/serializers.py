from rest_framework import serializers
from .models import *


class DocumentTextSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ['text',]
