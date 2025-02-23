from django.shortcuts import render
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(library=self.object)
        return context


# Register view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Create the new user
            login(request, user)  # Log the user in immediately after registration
            messages.success(request, 'Account created and logged in successfully!')
            return redirect('home')  # Redirect to a homepage or dashboard after login
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})


def is_admin(user):
    return user.groups.filter(name='Admin').exists()


def is_librarian(user):
    return user.groups.filter(name='Librarian').exists()


def is_member(user):
    return user.groups.filter(name='Member').exists()


@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome, Admin!")


@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome, Librarian!")


@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome, Member!")