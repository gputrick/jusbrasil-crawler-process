from rest_framework import serializers
from .models import Process, Move, RelatedPart, RelatedPeople

class RelatedPeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatedPeople
        fields = '__all__'

class RelatedPartSerializer(serializers.ModelSerializer):
    related_people = serializers.SerializerMethodField('get_related_people')

    def get_related_people(self, related_part):
        return RelatedPeopleSerializer(related_part.relatedpeople_set.all(), many=True).data

    class Meta:
        model = RelatedPart
        fields = '__all__'

class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = '__all__'

class ProcessSerializer(serializers.ModelSerializer):
    moves = serializers.SerializerMethodField('get_moves')
    related_parts = serializers.SerializerMethodField('get_related_parts')

    def get_moves(self, process):
        return MoveSerializer(process.move_set.all(), many=True).data

    def get_related_parts(self, process):
        return RelatedPartSerializer(process.relatedpart_set.all(), many=True).data

    class Meta:
        model = Process
        fields = '__all__'