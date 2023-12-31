from rest_framework import serializers

from todo_app.models import TodoModel


class TodoSerializer(serializers.ModelSerializer):
    due_date = serializers.DateTimeField()

    class Meta:
        model = TodoModel
        fields = ["title", "content", "due_date"]
