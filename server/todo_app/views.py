from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from todo_app.models import TodoModel
from todo_app.serializers import TodoSerializer


class TodoListCreateAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    queryset = TodoModel.objects.all()
    permission_classes = [SessionAuthentication]


class TodoRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    queryset = TodoModel.objects.all()
    permission_classes = [SessionAuthentication]
