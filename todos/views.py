from .models import Todo
from rest_framework import viewsets, permissions, status
from .serializers import TodoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TodoSerializer

    @action(detail=False, methods=['delete'])
    def completed(self, request):
        completed_todos = Todo.objects.filter(completed=True)
        completed_todos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
