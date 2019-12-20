from rest_framework import serializers
from .models import Process, Move, RelatedPart, RelatedPeople

class RelatedPeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatedPeople
        fields = '__all__'

class RelatedPartSerializer(serializers.ModelSerializer):
    related_people = RelatedPeopleSerializer(many=True)
    class Meta:
        model = RelatedPart
        fields = '__all__'

class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = '__all__'

class ProcessSerializer(serializers.ModelSerializer):
    moves = MoveSerializer(many=True)
    related_parts = RelatedPartSerializer(many=True)
    class Meta:
        model = Process
        fields = '__all__'