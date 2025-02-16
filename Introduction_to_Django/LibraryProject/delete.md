# Delete Operation

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