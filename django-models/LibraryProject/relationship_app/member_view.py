from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test


def is_member(user):
    return user.groups.filter(name='Member').exists()


@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome, Member!")