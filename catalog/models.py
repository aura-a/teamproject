from django.db import models
from django.urls import reverse # to generate URLs by reversing URL patterns


# Model representing a book
class Book(models.Model):

    # Fields
    title = models.CharField(max_length=200)
    # author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    author = models.CharField(max_length=200, null=False, default='No author', blank=False)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book.')
    quotes = models.TextField(max_length=2000, help_text='Enter some quotes from the book.', default="", blank=True)
    isbn = models.CharField(max_length=13,
                            help_text='13 character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number.</a>')
    # locations = models.ManyToManyField(Location)

    # Return the url to access a particular book instance
    def get_absolute_url(self):
        return reverse('book-details', args=[str(self.id)])

    def __str__(self):
        return self.title


# Model representing location
class Location(models.Model):

    # Fields
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True, null=True, help_text='A short description of the location.')

    class Meta:
        ordering = ["name", "country"]

    def get_absolute_url(self):
        return reverse('location-details', args=[str(self.id)])

    def __str__(self):
        return f'{self.name} ,{self.country}'

