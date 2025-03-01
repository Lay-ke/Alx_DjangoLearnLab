# Create Operation

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