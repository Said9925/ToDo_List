from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.title