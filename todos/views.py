from .models import Todo
from rest_framework import viewsets, permissions, status
from .serializers import TodoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = TodoSerializer

    def get_queryset(self):
        return self.request.user.todos.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False, methods=['delete'])
    def completed(self, request):
        completed_todos = Todo.objects.filter(
            Q(completed=True) | Q(parentTodo__completed=True))
        completed_todos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
