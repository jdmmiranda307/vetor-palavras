from django.db import models

# Create your models here.
class SequenceDefault(models.Model):
    word = models.CharField(max_length=50, null=False, blank=False, unique=True)


class Sequence2Gram(models.Model):
    words = models.CharField(max_length=100, null=False, blank=False, unique=True)


class DocumentSequence2Grams(models.Model):
    document = models.ForeignKey('Document', on_delete=models.DO_NOTHING)
    sequence_2gram = models.ForeignKey('Sequence2Gram', on_delete=models.DO_NOTHING)


class DocumentSequenceDefault(models.Model):
    document = models.ForeignKey('Document', on_delete=models.DO_NOTHING)
    sequence_default = models.ForeignKey('SequenceDefault', on_delete=models.DO_NOTHING)


class Document(models.Model):
    text = models.TextField(null=False, blank=False)
    sequence_defaults = models.ManyToManyField(SequenceDefault, through=DocumentSequenceDefault)
    sequence_2grams =  models.ManyToManyField(Sequence2Gram, through=DocumentSequence2Grams)
