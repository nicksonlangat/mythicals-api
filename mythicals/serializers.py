from rest_framework import serializers

from .models import Mythical

class MythicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mythical
        fields = [
            'id',
            'title',
            'first_description',
            'second_description',
            'third_description',
            'first_image',
            'second_image',
            'third_image',
            'created_at',
            'is_trending'
        ]