from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    link = models.CharField(max_length=254, default="http://google.com")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
