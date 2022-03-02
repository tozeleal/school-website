from django.db import models

# Create your models here.

class book(models.Model):
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=10)
    book_price = models.IntegerField()
    book_quantity = models.IntegerField()

    # String representation
    def __str__(self):
        return self.book_name

