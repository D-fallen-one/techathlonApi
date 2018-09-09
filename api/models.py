from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Books(models.Model):
    isbn = models.CharField(max_length=200, primary_key = True)
    booktitle = models.CharField(max_length=100)
    bookAuthor = models.CharField(max_length=100)
    yearOfPublication = models.IntegerField(validators = [MaxValueValidator(10), MinValueValidator(0)])
    publisher = models.CharField(max_length=100)
    imageUrlS = models.CharField(max_length=250)
    imageUrlM = models.CharField(max_length=250)
    imageUrlL = models.CharField(max_length=250)
    avgRating = models.FloatField(validators = [MaxValueValidator(10), MinValueValidator(0)])
    rateCount = models.IntegerField(validators = [MaxValueValidator(10), MinValueValidator(0)])

    def __str__(self):
        return self.isbn

class Ratings(models.Model):
    isbn = models.ForeignKey(Books, on_delete = models.CASCADE)
    rating = models.IntegerField(validators = [MaxValueValidator(10), MinValueValidator(0)])