from relationship_app.models import Author, Book, Library, Librarian

# List all bookd in a library
library_name="Sam Jonah Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

# Query all books by a specific author
author_name = 'Pascal'  
author = Author.objects.get(name=author_name)
# Filter books by a specific author
filtered_books = Book.objects.filter(author=author)
print(filtered_books)


# Retrieve the librarian of a library
librarian = Librarian.objects.get(library=library_name)