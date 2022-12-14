from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ("id","title","description","image","likes", "views")
        read_only_fields = ("id","likes","views")