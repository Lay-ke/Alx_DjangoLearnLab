from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render


def is_admin(user):
    return user.groups.filter(name='Admin').exists()


@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


