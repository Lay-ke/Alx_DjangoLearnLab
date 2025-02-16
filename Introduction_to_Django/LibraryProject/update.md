# Update Operation

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