from django.contrib import admin

from .models.perk import Perk
from .models.character_class import CharacterClass

# Register your models here.
admin.site.register(Perk)
admin.site.register(CharacterClass)
