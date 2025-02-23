from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test, login_required

def is_librarian(user):
    return user.groups.filter(name='Librarian').exists()

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome, Librarian!")