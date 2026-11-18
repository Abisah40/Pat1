from rest_framework import serializers
from .models import CreateProperty

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateProperty
        fields = '__all__'
        read_only_fields = ('created_at','update_at',)