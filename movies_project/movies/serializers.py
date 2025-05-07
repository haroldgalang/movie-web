from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
        extra_kwargs = {"poster": {"required": False, "allow_null": True}}
