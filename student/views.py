from django.shortcuts import render
from .models import Student
from django.db import connection
from django.db.models import Q

# Part 2
#################################################################


def student_list_(request):

    posts = Student.objects.all()
    print(posts)  # All objects in table
    print(posts.query)  # SQL statement
    print(connection.queries)  # Whole query , Time and Limit also mentioned
    return render(request, 'output.html', {'posts': posts.query})


def student_list_(request):
    posts = Student.objects.filter(
        Q(surname__startswith='austin') | ~Q(surname__startswith='baldwin'))

    print(posts)
    print(posts.query)

    return render(request, 'output.html', {'posts': posts})


def student_list(request):
    posts = Student.objects.filter(
        Q(classroom=3) & Q(firstname__startswith='lakisha'))

    print(posts)
    print(connection.queries)

    return render(request, 'output.html', {'posts': posts})
