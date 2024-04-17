from rest_framework import serializers

from .models import Chair

class ChairSerializer(serializers.Serializer):
    class Meta: 
        model = Chair
        fields = "__all__"