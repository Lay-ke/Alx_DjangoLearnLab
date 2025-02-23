from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test, login_required


def is_admin(user):
    return user.groups.filter(name='Admin').exists()

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome, Admin!")


