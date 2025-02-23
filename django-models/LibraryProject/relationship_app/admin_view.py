from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.groups.filter(name='Admin').exists()

@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome, Admin!")


