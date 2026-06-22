from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

class Book(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

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
    imprint = models.CharField(Author, on_delete=models.CASCADE)
    due_back = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default=RETURNED)
