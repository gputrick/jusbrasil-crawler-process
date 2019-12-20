from rest_framework import serializers
from .models import Process, Move


class MoveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Move
        fields = '__all__'

class ProcessSerializer(serializers.HyperlinkedModelSerializer):
    moves = MoveSerializer(many=True)
    class Meta:
        model = Process
        fields = '__all__'