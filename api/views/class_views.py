from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.character_class import CharacterClass
from ..serializers import ClassSerializer


class CharacterClasses(generics.ListCreateAPIView):
    serializer_class = ClassSerializer

    def get(self, request):
        """Index request"""
        data = ClassSerializer(CharacterClass, many=True).data
        return Response({'classes': data})


class ClassDetail(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, pk):
        """Show request"""
        character_class = get_object_or_404(CharacterClass, pk=pk)
        data = ClassSerializer(character_class).data
        return Response({'class': data})

    def delete(self, request, pk):
        """Delete request"""
        character_class = get_object_or_404(CharacterClass, pk=pk)
        character_class.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update request"""
        character_class = get_object_or_404(CharacterClass, pk=pk)
        temp_class = request.data['class']
        data = ClassSerializer(character_class, data=temp_class)

        if data.is_valid():
            data.save()
            return Response({'class': data}, status=status.HTTP_202_ACCEPTED)

        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
