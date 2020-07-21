from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=100)
    post = models.TextField(max_length=400)
    link = models.CharField(max_length=254, default='http://google.com')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']