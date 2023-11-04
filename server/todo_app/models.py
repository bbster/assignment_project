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
