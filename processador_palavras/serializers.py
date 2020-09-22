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


class DocumentDefaultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = '__all__'
        depth = 1


    def to_representation(self, data):
        response = {'documents': []}
        for doc in data:
            temp_dict = {
                'document': doc.id,
                'text': doc.text,
                'vocabulary': [default.word for default in doc.sequence_defaults.all()]
            }
            response['documents'].append(temp_dict)
        return response
