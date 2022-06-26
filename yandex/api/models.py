from django.db import models
import uuid

class Main(models.Model):
    uid = models.UUIDField(unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    parentId = models.ForeignKey('Main', on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    updateDate = models.DateTimeField()
    def __str__(self):
        return self.name

