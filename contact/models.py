from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
