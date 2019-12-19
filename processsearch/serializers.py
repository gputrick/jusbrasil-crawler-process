from rest_framework import serializers
from .models import Process, Move


class MoveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Move
        fields = ['date', 'description']

class ProcessSerializer(serializers.HyperlinkedModelSerializer):
    moves = MoveSerializer(many=True)
    class Meta:
        model = Process
        fields = ['process', 'classe', 'subject', 'distribuition', 'control', 'judge', 'action_value', 'moves' ]