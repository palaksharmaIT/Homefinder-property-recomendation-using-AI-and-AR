from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'
        read_only_fields = ['posted_by', 'posted_on']

    def create(self, validated_data):
        validated_data['posted_by'] = self.context['request'].user
        return super().create(validated_data)

 