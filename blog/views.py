from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import posts

# Create your views here.
    

def index(request):
    tweets = posts.objects.all().order_by("-pub_date",'-pub_time')
    print(type(tweets))
    return render(request, 'blog/index.html', {'tweets': tweets})
def create_post(request):
    author=request.POST.get('author','anonymus')
    content=request.POST.get('content')
    posts.objects.create(author_name=author,content=content)
    return redirect("Twitter-clone")