from django.db import models


class Todo(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False, unique=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateTimeField(null=False, blank=False)
    finished_at = models.DateTimeField(null=True)
