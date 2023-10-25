from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from todo.models import TodoModel
from todo.serializers import TodoSerializer


class TodoListCreateAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    queryset = TodoModel.objects.all()


class TodoRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    queryset = TodoModel.objects.all()
