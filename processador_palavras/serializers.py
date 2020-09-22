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


class SequenceDefaultSerializer(serializers.ModelSerializer):

    class Meta:
        model = SequenceDefault
        fields = '__all__'


class Sequence2GramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sequence2Gram
        fields = '__all__'
