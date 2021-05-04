from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.perk import Perk
from ..serializers import PerkSerializer


class Perks(generics.ListCreateAPIView):
    serializer_class = PerkSerializer

    def get(self, request, cc):
        """Index request"""
        perk = Perk.objects.filter(character_class=cc)
        data = PerkSerializer(perk, many=True).data
        return Response({'perks': data})


class PerkDetail(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, pk):
        """Show request"""
        class_perk = get_object_or_404(Perk, pk=pk)
        data = PerkSerializer(class_perk).data
        return Response({'perk': data})

    def delete(self, request, pk):
        """Delete request"""
        class_perk = get_object_or_404(Perk, pk=pk)
        class_perk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update request"""
        class_perk = get_object_or_404(Perk, pk=pk)
        temp_perk = request.data['data']
        data = PerkSerializer(class_perk, data=temp_perk)

        if data.is_valid():
            data.save()
            return Response({'perk': data}, status=status.HTTP_202_ACCEPTED)

        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
