from rest_framework import serializers

from categories.models import Category
from ..models import Task


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    category = serializers.SlugRelatedField(
        slug_field='uid',
        queryset=Category.objects.all(),
    )

    class Meta:
        model = Task
        fields = [
            "uid",
            "name",
            "description",
            "author",
            "category",
            "is_completed",
            "date",
            "created",
            "modified",
        ]
