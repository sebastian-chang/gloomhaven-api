from django.db import models
from django.contrib.postgres.fields import ArrayField


class CharacterClass(models.Model):
    class_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    initials = models.CharField(max_length=5)
    starting = models.BooleanField(default=False)
    symbol = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    xp_per_level = ArrayField(models.IntegerField())
    hp_per_level = ArrayField(models.IntegerField())
    story = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    def as_dict(self):
        return {
            'class_name': self.class_name,
            'name': self.name,
            'initials': self.initials,
            'is_starting': self.starting,
            'symbol': self.symbol,
            'image': self.image,
            'logo': self.logo,
            'color': self.color,
            'xp': self.xp_per_level,
            'hp': self.hp_per_level,
            'story': self.story,
        }
