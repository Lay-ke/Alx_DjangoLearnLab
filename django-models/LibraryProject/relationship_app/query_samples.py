from relationship_app.models import Author, Book, Library, Librarian

# List all bookd in a library
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

# Query all books by a specific author
author  = Author.objects.get(name='J.K. Rowling')
books = author.books.all()
print(books)



# Retrieve the librarian of a library
librarian = Librarian.objects.get(name='Joel')