from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Category
from .forms import BookForm
from .view_helpers import book_is_favorited
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect("index")
    return render(request, "home.html")

@login_required
def index(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    return render(request, "index.html", {"books": books, "categories": categories})

@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    favorited = book_is_favorited(book, request.user)
    form = BookForm()
    return render(request, "book_detail.html", {"book": book, "pk": pk, "form": form, "favorited": favorited})

def add_book(request):
    if request.method =='GET':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='index')
    return render(request, "add_book.html", {"form": form})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        form = BookForm(instance=book)
    else:
        form = BookForm(data=request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(to="index")
    return render(request, "edit_book", {"book": book, "form": form, "pk": pk})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect(to='index')
    return render(request, "delete_book.html", {"book": book, "pk": pk})

def title(request):
    title = Book.objects.order_by('title')
    categories = Category.objects.all()
    context = {'books': title, 'categories': categories}
    return render(request, 'index.html', context)

@login_required
def oldest(request):
    oldest = Book.objects.order_by('created_at')
    categories = Category.objects.all()
    context = {'books': oldest, 'categories': categories}
    return render(request, 'index.html', context)

@login_required
def newest(request):
    newest = Book.objects.order_by('-created_at')
    categories = Category.objects.all()
    context = {'books': newest, 'categories': categories}
    return render(request, 'index.html', context)

@login_required
def add_favorite(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    user = request.user
    user.favorite_books.add(book)
    return redirect("book_detail", pk=book.pk)

@login_required
def delete_favorite(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    request.user.favorite_books.remove(book)
    return redirect("book_detail", pk=book.pk)

@login_required
def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    books = category.books.all()
    return render(request, "category.html", {"category": category, "books": books})