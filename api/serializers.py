from rest_framework import serializers
from .models import Wine

class WineSerializer(serializers.Serializer):
    name = serializers.CharField()
    vinyard = serializers.CharField()
    year = serializers.IntegerField()
    gwscore = serializers.IntegerField()

    def create(self, validated_data):
        return Wine.object.create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.vineyard = validated_data.get('vinyard', instance.vinyard)
        instance.year = validated_data.get('year', instance.year)
        instance.gwscore = validated_data.get('gwscore', instance.gwscore)
