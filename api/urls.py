from django.urls import path

from .views.class_views import CharacterClasses, ClassDetail
from .views.perk_views import Perks, PerkDetail

urlpatterns = [
    path('classes/', CharacterClasses.as_view(), name='classes'),
    path('classes/<int:pk>', ClassDetail.as_view(), name='class_detail'),
    path('perks/', Perks.as_view(), name="perks"),
    path('perks/<int:pk>', PerkDetail.as_view(), name='perk_detail'),
]
