from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Book

def home(request):
    books = Book.objects.all().order_by('-created_at')
    
    context = {
        'books': books
    }
    return render(request, 'books/home.html', context)


def detail_book(request, id):
    book = get_object_or_404(Book, id=id)

    context = {
        'book': book
    }
    return render(request, 'books/detail_book.html', context)