from django.shortcuts import render
from .models import Post, Tag
from django.views.generic import View


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})

#def post_detail(request, slug):
 #   post = Post.objects.get(slug__iexact=slug)
  #  return render(request, 'blog/post_detail.html', context={'post': post})

class PostDetail(View):
    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        return render(request, 'blog/post_detail.html', context={'post': post})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})

class TagDetail(View):
    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        return render(request, 'blog/tag_detail.html', context={'tag': tag})

#def tag_detail(request, slug):
#    tag = Tag.objects.get(slug__iexact=slug)
#    return render(request, 'blog/tag_detail.html', context={'tag': tag})