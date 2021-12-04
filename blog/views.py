from django.shortcuts import render, get_object_or_404
from .models import Post, Category
# Create your views here.

def index(request):
    posts = Post.objects.order_by('-date')
    context = {
        'posts' : posts
    }
    return render(request,'blog/index.html', context)


def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request,'blog/contact.html')

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'blog/detail.html',context)