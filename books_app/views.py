from django.shortcuts import render, redirect
from .models import BooksModel, Tag


def loadBooksPage(request):
    books = BooksModel.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'pages/books.html', context)



def loadSingleBookPage(request, slug):
    book = BooksModel.objects.get(slug=slug)
    context = {
        'book': book
    }

    return render(request, 'pages/book.html', context)