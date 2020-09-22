import re
from collections import Counter
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .stop_words import STOP_WORDS
from .models import *
from .serializers import *

# Create your views here.
class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentTextSerializer
    queryset = Document.objects.all()
    http_method_names = ['get', 'post', 'head']


    def create(self, request, *args, **kwargs):
        try:
            texts = request.data['texts']
            serializer = self.get_serializer(data=texts, many=True)
            if serializer.is_valid():
                serializer.save()
                texts = [i['text'] for i in texts]
                for i, text in enumerate(texts):
                    words = self._text_cleaner(text)
                    vocabulary_tuple = self._get_vocabulary(words)
                    instance = serializer.instance[i]
                    for word in vocabulary_tuple[1]:
                        self._save_relation_data({'word':word}, SequenceDefaultSerializer, instance)
                        self._create_document_sequence_default(instance, word)

                    for words in vocabulary_tuple[0]:
                        words = ' '.join(words)
                        self._save_relation_data({'words': words}, Sequence2GramSerializer, instance)
                        self._create_document_sequence_s2gram(instance, words)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'msg': str(e)}, status=status.HTTP_400_BAD_REQUEST) 


    def _save_relation_data(self, data, serializer, instance):
        instance_serializer = serializer(data=data)
        if instance_serializer.is_valid(raise_exception=False):
            instance_serializer.save()


    def _text_cleaner(self, texts):
        stop_words_dict = Counter(STOP_WORDS)
        text = [word for word in texts.split() if word not in stop_words_dict]
        return text


    def _get_vocabulary(self, words):
        gram2 = list(zip(words, words[1:]))
        default = list(words)
        return (gram2, default)


    def _create_document_sequence_default(self, doc_instance, word):
        obj = SequenceDefault.objects.get(word=word)
        document_default_data = {'document': doc_instance.id, 'sequence_default': obj.id}
        document_default_serializer = DocumentSequenceDefaultSerializer(data=document_default_data)
        if document_default_serializer.is_valid(raise_exception=False):
            document_default_serializer.save()


    def _create_document_sequence_s2gram(self, doc_instance, words):
        obj = Sequence2Gram.objects.get(words=words)
        document_2gram_data = {'document': doc_instance.id, 'sequence_2gram': obj.id}
        document_2gram_serializer = DocumentSequence2GramsSerializer(data=document_2gram_data)
        if document_2gram_serializer.is_valid(raise_exception=False):
            document_2gram_serializer.save()


class SequenceDefaultViewSet(viewsets.ModelViewSet):
    serializer_class = SequenceDefaultSerializer
    queryset = SequenceDefault.objects.all()
    http_method_names = ['get', 'head']


class Sequence2GramViewSet(viewsets.ModelViewSet):
    serializer_class = Sequence2GramSerializer
    queryset = Sequence2Gram.objects.all()
    http_method_names = ['get', 'head']


class DocumentSequenceDefaultViewSet(APIView):
    http_method_names = ['get', 'head']

    def get(self, request):
        try:
            documents = Document.objects.all()
            if documents:
                serializer = DocumentDefaultSerializer(documents)
                data = serializer.data
                status_code = status.HTTP_200_OK
                return Response(data, status=status_code)
            else:
                return Response({'msg': 'error 404 not found'}, status=status.HTTP_404_NOT_FOUND)
        except AttributeError as e:
            return Response({'msg': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DocumentSequence2GramViewSet(APIView):
    http_method_names = ['get', 'head']

    def get(self, request):
        try:
            documents = Document.objects.all()
            if documents:
                serializer = Document2GramsSerializer(documents)
                data = serializer.data
                status_code = status.HTTP_200_OK
                return Response(data, status=status_code)
            else:
                return Response({'msg': 'error 404 not found'}, status=status.HTTP_404_NOT_FOUND)
        except AttributeError as e:
            return Response({'msg': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
