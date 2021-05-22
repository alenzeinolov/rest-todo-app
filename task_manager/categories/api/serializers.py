from rest_framework import serializers

from ..models import Category


class CategorySerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = Category
        fields = [
            "uid",
            "name",
            "author",
            "created",
            "modified",
        ]
