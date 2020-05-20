from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def index(request):
    # return HttpResponse("HELLO FROM POST")
    post = Post.objects.all()[:10]

    context ={
        'title' :'Latest Post',
        'post': post
    }
    return render(request,'post/index.html',context)

def details(request,id):
    post =Post.objects.get(id=id)

    context ={
        'post': post
    }
    return render(request,'post/details.html',context)