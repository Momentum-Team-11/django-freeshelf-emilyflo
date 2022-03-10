def book_is_favorited(book, user):
    return user.favorite_books.filter(pk=book.pk).exists()