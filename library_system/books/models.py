from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=255, blank=False, verbose_name="First Name")
    last_name = models.CharField(max_length=255, blank=False, verbose_name="Last Name")
    date_of_birth = models.DateField(auto_now=True)
    date_of_death = models.DateField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255, blank=False, verbose_name="Book Title")
    summary = models.TextField(max_length=255, blank=True, verbose_name="Book Summary")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class BookInstance(models.Model):
    RETURNED = 'RET'
    BORROWED = 'BOR'
    OVERDUE = 'DUE'

    STATUS_CHOICES = {
        RETURNED: 'returned',
        BORROWED: 'borrowed',
        OVERDUE: 'overdue'
    }

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    imprint = models.ForeignKey(Author, on_delete=models.CASCADE)
    due_back = models.DateField(auto_now=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default=RETURNED)
