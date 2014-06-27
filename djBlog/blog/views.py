from django.shortcuts import render, get_object_or_404
from blog.models import Post

def index(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'blog/index.html', {'posts': posts})

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post.html', {'post': post})

def loop_times():
    context['loop_times'] = [i+1 for i in range (1)]