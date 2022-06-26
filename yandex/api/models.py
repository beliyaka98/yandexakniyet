from django.db import models
import uuid

class Main(models.Model):
    uid = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    parentId = models.ForeignKey('Main', on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    updateDate = models.DateTimeField()
    def __str__(self):
        return self.name

