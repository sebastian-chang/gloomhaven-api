from django.db import models


class Perk(models.model):
    id = models.CharField(max_length=20)
    quantity = models.IntegerField()
    action = models.CharField(max_length=100)
    character_class = models.ForeignKey(
        'Class',
        related_name='perks',
        null=True,
        on_delete=models.CASCADE,
    )

    def as_dict(self):
        return {
            'id': self.id,
            'quantity': self.quantity,
            'action': self.action,
        }
