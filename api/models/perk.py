from django.db import models


class Perk(models.Model):
    perk_id = models.CharField(max_length=20)
    quantity = models.IntegerField()
    action = models.CharField(max_length=100)
    character_class = models.ForeignKey(
        'CharacterClass',
        related_name='perks',
        null=True,
        on_delete=models.CASCADE,
    )

    def as_dict(self):
        return {
            'id': self.perk_id,
            'quantity': self.quantity,
            'action': self.action,
        }
