from rest_framework import serializers

from .models.perk import Perk
from .models.character_class import CharacterClass


class PerkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perk
        fields = ('id', 'quantity', 'action')


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterClass
        fields = ('class_name', 'name', 'initials', 'is_starting',
                  'symbol', 'image', 'logo', 'color', 'xp', 'hp', 'story', 'perks')
