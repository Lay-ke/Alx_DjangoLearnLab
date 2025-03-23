from django.shortcuts import render
from .forms import UserRegisterForm

# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

def profile(request):
    if request.method == 'PUT':
        form = UserRegisterForm(request.PUT, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UserRegisterForm()
    return render(request, 'blog/profile.html', {'form': form})