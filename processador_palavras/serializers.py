from rest_framework import serializers
from .models import *


class DocumentTextSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ['text',]


class DocumentSequenceDefaultSerializer(serializers.ModelSerializer):

    class Meta:
        model = DocumentSequenceDefault
        fields = '__all__'


class DocumentSequence2GramsSerializer(serializers.ModelSerializer):

    class Meta:
        model = DocumentSequence2Grams
        fields = '__all__'