from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    author_name = models.CharField(max_length=200)
    publisher = models.CharField(max_length=100)
    pages_quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
