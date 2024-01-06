from rest_framework import serializers
from devices import models

class ScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Scale
        fields = ['id', 'name', 'port', 'protocol']