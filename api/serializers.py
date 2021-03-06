from rest_framework import serializers

from .models.perk import Perk
from .models.character_class import CharacterClass


class PerkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perk
        fields = ('perk_id', 'quantity', 'action')


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterClass
        fields = ('class_name', 'name', 'initials', 'starting',
                  'symbol', 'image', 'logo', 'color', 'xp_per_level', 'hp_per_level', 'story', 'perks')
