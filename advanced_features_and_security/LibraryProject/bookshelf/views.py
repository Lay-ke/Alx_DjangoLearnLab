from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden, HttpResponse
from .models import Book
from .forms import ExampleForm, BookForm  # Import ExampleForm

def add_csp_header(response):
    response['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; style-src 'self';"
    return response

# View for displaying a single book
@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    response = render(request, 'bookshelf/book_detail.html', {'book': book})
    return add_csp_header(response)

# View for creating a new book
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to the list of books after creation
    else:
        form = BookForm()
    response = render(request, 'bookshelf/book_form.html', {'form': form})
    return add_csp_header(response)

# View for editing an existing book
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = BookForm(instance=book)
    response = render(request, 'bookshelf/book_form.html', {'form': form})
    return add_csp_header(response)

# View for deleting a book
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to the list of books after deletion
    response = render(request, 'bookshelf/book_confirm_delete.html', {'book': book})
    return add_csp_header(response)

# List all books (no permissions required for this, but you can add one if needed)
def book_list(request):
    books = Book.objects.all()
    response = render(request, 'bookshelf/book_list.html', {'books': books})
    return add_csp_header(response)

# New view for handling ExampleForm
def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page after form submission
    else:
        form = ExampleForm()
    response = render(request, 'bookshelf/form_example.html', {'form': form})
    return add_csp_header(response)
