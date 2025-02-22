from relationship_app.models import Author, Book, Library, Librarian

# # Create an author
# author = Author.objects.create(name='J.K. Rowling')

# # Create a book
# book = Book.objects.create(title='Harry Potter and the Philosopher\'s Stone', author=author)

# # Create a library
# library = Library.objects.create(name='Sam Jonah Library')

# # Add the book to the library
# library.books.add(book)

# # Create a librarian
# librarian = Librarian.objects.create(name='Joel', library=library)


# List all bookd in a library
library = Library.objects.get(name='library_name')
books_in_library = library.books.all()

# Query all books by a specific author
author  = Author.objects.get(name='J.K. Rowling')
books = author.books.all()
print(books)



# Retrieve the librarian of a library
librarian = Librarian.objects.get(name='Joel')