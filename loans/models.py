from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth.models import User

from books.models import Book


class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    return_at = models.DateField(null=True)

    def save( self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.return_at = datetime.today().date() + timedelta(days=7)
        super(Loan, self).save()