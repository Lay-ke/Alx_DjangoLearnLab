# Retrieve Operation

### Command:
```python
# Retrieve all books
books = Book.objects.get(title="1984")

# Display the books
books
```

### Expected Output
`<QuerySet [<Book: 1984>]>  # This will show a list of all Book instances, including the one we just created.`