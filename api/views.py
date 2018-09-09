from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from . import models
import numpy as numpy
import pandas as pd

def default(request):
    data = {
        'name': 'default',
        'function': 'api callback test',
        'status': 'OK',
    }
    return JsonResponse(data)

def defaultWithParams(request,to,frm):
    print(to)
    data = {
        'to': to,
        'from': frm,
    }
    return JsonResponse(data)


# Add the code to top 10 books suggestions
def top10(request):
    pass


# Add the code for the changeing the rating
def editRating(request, isbn, rating):
    pass


# Add the code for user based recommandation
def userBasedRecommandation(request, user):
    pass


# Add the code for item based recommandation
def itemBasedRecommandation(request, isbn):
    pass


# Login Function
def login(request, user, password):
    u = User.objects.get(username = user)
    if u.username == user :
        data = {
            'status': 'valid'
        }
    else :
        data = {
            'status': 'invalid'
        }

    return JsonResponse(data)


# creating new user
# returns a JSON with key status and value created
def createUser(request, user, password, email):
    User.objects.create_user(user, email,password)
    return JsonResponse({'status': 'created'})


# function which return json object of detailed books
def bookdetails(request, isbn):
    books = models.Books.objects.get(isbn = isbn)
    data = {
        'title': books.booktitle,
        'isbn': books.isbn,
    }
    return JsonResponse(data)