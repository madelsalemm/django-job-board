from .models import job
from rest_framework import serializers

# Serializers define the API representation.
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = job
        fields = '__all__'
