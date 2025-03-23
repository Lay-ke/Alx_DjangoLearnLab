from django.shortcuts import render
from .forms import UserRegisterForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Blog, Post
from .models import Comment
from .forms import CommentForm
from django.db.models import Q

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


class PostListView(ListView):
    model = Blog
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Blog


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

class CommentListView(ListView):
    model = Comment
    template_name = 'blog/comments.html'
    context_object_name = 'comments'
    ordering = ['-date_posted']
    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs['post_id'])
    

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['post_id']
        return super().form_valid(form)
    def get_success_url(self):
        return self.object.post.get_absolute_url()
    

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False
    def get_success_url(self):
        return self.object.post.get_absolute_url()
    

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False
    def get_success_url(self):
        return self.object.post.get_absolute_url()
    

class PostSearchView(ListView):
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Blog.objects.filter(
                Q(title__icontains=query) | 
                Q(content__icontains=query) | 
                Q(tags__name__icontains=query)
            ).distinct()
        return Blog.objects.none()
    
class PostsByTagListView(ListView):
    model = Blog
    template_name = 'posts_by_tag.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag_name = self.kwargs['tag_name']
        return Blog.objects.filter(tags__name=tag_name)