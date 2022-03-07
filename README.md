# Freeshelf

This week, you are building a Django application to collect an index of free programming books online. You'll work on this application for the entire week. The end goal is an application that allows users to see a list of all the books, register and log in, and favorite books.

## Requirements and goals

### Overall requirements

- Your application should be styled. It should be usable and aesthetically neutral, at a minimum. There is a sample mockup of the index page in [mockup/index.html](mockup/index.html). You do not have to follow this mockup -- it's just a place to start if you don't have your own ideas.
- When you are not sure about whether a feature is needed, use your knowledge of similar sites and your good sense.
- A starter project and app are provided, along with a custom user model and the accompanying migration.

### Goal 1: books

Your first goal should be creating a Book model and showing an index of all books. Some details:

- Books have, at a minimum, a title, author, description, URL, and date added to the database (`created_at`).
- Book URLs (the URL field in the database) should be unique.
- Admins can add, edit, and delete books.
- You should have initial data for books (a CSV is provided, but you can edit it to fit your data).
- Books should be displayed in order with the most recently added at the top.

#### Initial Data

To load some initial books into your database, you can [create a data migration](https://docs.djangoproject.com/en/4.0/topics/migrations/#data-migrations). Read the data from the CSV file and use your model to save data to the database. ([Another good resource on data migrations.](https://simpleisbetterthancomplex.com/tutorial/2017/09/26/how-to-create-django-data-migrations.html))

You can also create books using the Django admin.

#### Stretch for Goal 1

- Add an optional image url for books.
- Allow users to change the sorting order of books, ordering by title or by reverse order of being added.

### Goal 2: registration and login

Your next goal is adding registration and login to your application. Change the flow of your application so that users have to log in to see their books.

If a user is not logged in, they should see the log in page (a form to log in).

The user should be able to click on links to log in or register, and to log out if they are logged in.

### Goal 3: associated categories

Your next goal should be adding categories for books. Each book should be associated with a category.

- Categories have a title and a [slug](https://docs.djangoproject.com/en/4.0/ref/models/fields/#slugfield).
- Each category should have a URL that shows books just for that category. For example: `books/python` or `books/javascript`.

#### Stretch for Goal 3

- Allow books to be in more than one category.

### Goal 4: user favorites

Once you have registration and login, users should be able to nark books as their favorites. Every user should be able to go to a URL, `/favorites/`, to see their favorite books. The books should be in order with the most recently favorited ones on top. The user can "un-favorite" a currently favorited book.

#### Stretch for Goal 4

- Show the number of times a book has been favorited on its entry.


### 🌶 Spicy Features

If you reach the four goals above, challenge yourself to implement these additional features.
#### 🌶 Spicy Goal 1: Add user comments

Users should be able to comment on books. Each book will need to have its own unique URL where you can see comments on the book. Comments should be in order from the oldest to the newest. On book listing pages (the main page and the category pages), the number of comments should be listed with the book.

##### Stretch for 🌶 Goal 1

- Make user names on comments links to a user profile page. This page should show all the comments the user has made on all books.

#### 🌶 Spicy Goal 2: Users can suggest books

Users should be able to suggest new books for Freeshelf. You can do this with a separate Suggestion model or by using the Book model with a new boolean indicating whether the suggestion has been accepted or not. Either way, a new page, `/suggestions/`, should be available to admins, showing them all the current suggestions and allowing them to accept or decline the suggestion.

## Project Setup

This project makes some additions and modifications to the defaults in Django:

- There is a custom user model defined in `books.models.User`.
- There are a `templates/` and a `static/` directory at the top level, both of which are configured (in `settings.py`) to be used.
- A `.gitignore` file is provided.
- [Pipenv](https://pipenv.pypa.io/en/latest/) is used to manage dependencies.

The following dependencies are included:

- [django-extensions](https://django-extensions.readthedocs.io/en/latest/) and [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) are both installed and configured to be used.
- [django-environ](https://django-environ.readthedocs.io/en/latest/) is set up and the `DEBUG`, `SECRET_KEY`, and `DATABASES` settings are set by this package. A `.env.sample` file is included, and should be copied to create a local `.env` file.

### Steps after cloning this project repo

```sh
$ pipenv install
$ cp django_freeshelf/.env.sample django_freeshelf/.env
$ pipenv shell
$ ./manage.py migrate
$ ./manage.py createsuperuser # follow prompts to create a superuser
$ ./manage.py runserver
```

## Resources

- [Free Programming Books GitHub Repo](https://github.com/EbookFoundation/free-programming-books)
