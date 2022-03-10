from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    URL = models.URLField(max_length=200, blank=True)
    imageUrl = models.ImageField(blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    favorited_by = models.ManyToManyField(User, related_name = "favorite_books")
    category = models.ManyToManyField("Category", related_name="books")

    def __str__(self):
        return self.title
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True, blank=True, unique=True)

    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Category name=(self.name)>"

    def save(self):
        self.slug = slugify(self.name)
        super().save()