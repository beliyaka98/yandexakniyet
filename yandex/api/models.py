from django.db import models


class Main(models.Model):
    id = models.UUIDField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    parentId = models.ForeignKey('Main', on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    updateDate = models.DateTimeField()
    def __str__(self):
        return self.name

