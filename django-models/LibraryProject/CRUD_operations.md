# Database Operations

1. Create Operation

### Command:
```python
# Import the Book model
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Display the created book
book
```

### Expected Output
`<Book: 1984>  # The output will show the Book object with its string representation`

---

2. Retrieve Operation

### Command:
```python
# Retrieve all books
books = Book.objects.all()

# Display the books
books
```

### Expected Output
`<QuerySet [<Book: 1984>]>  # This will show a list of all Book instances, including the one we just created.`

---

3. Update Operation

### Command:
```python
# Retrieve the book instance to update
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Display the updated book
book
```

### Expected Output
`<Book: Nineteen Eighty-Four>  # This will show that the book's title has been updated successfully.`

---

4. Delete Operation

### Command:
```python
# Retrieve the book to delete
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Verify deletion by retrieving all books
Book.objects.all()
```

### Expected Output
`<QuerySet []>  # This confirms that no books are left in the database after deletion.`

