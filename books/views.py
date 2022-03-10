from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Category
from .forms import BookForm

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect("index")
    return render(request, "home.html")

def index(request):
    books = Book.objects.all()
    categorys = Category.objects.all()
    return render(request, "index.html", {"books": books, "categorys": categorys})

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
    context = {'books': title}
    return render(request, 'index.html', context)

def oldest(request):
    oldest = Book.objects.order_by('created_at')
    context = {'books': oldest}
    return render(request, 'index.html', context)

def newest(request):
    newest = Book.objects.order_by('-created_at')
    context = {'books': newest}
    return render(request, 'index.html', context)

def book_is_favorited(book, user):
    return user.favorite_books.filter(pk=book.pk)

# def add_favorite(request, book):
#     book = get_object_or_404(Book, pk=book.pk)
#     user = request.user
#     user.favorite_books.add(book)
#     favorited = book_is_favorited(book, request.user)
#     return redirect("book_detail", pk = book.pk)

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    books = category.books.all()
    return render(request, "category.html", {"category": category, "books": books})