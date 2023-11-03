from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TodoModel(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    due_date = models.DateTimeField()


class A(models.Model):
    name = models.CharField(max_length=100)
    b = models.ForeignKey(
        "todo_app.B", on_delete=models.CASCADE, related_name="a_set", null=True
    )


class B(models.Model):
    name = models.CharField(max_length=100, null=True)
