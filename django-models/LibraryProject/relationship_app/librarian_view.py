from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

def is_librarian(user):
    return user.groups.filter(name='Librarian').exists()

@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome, Librarian!")