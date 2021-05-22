from rest_framework import permissions, viewsets

from .serializers import TaskSerializer
from ..models import Task


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "uid"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related("category")
        qs = qs.filter(author=self.request.user)
        return qs
