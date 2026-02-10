from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article


POSTS = [
    {
        'author': '<DevsMentoring>',
        'title': 'To be or not to be',
        'content': "That's my first post",
        'date': '28 April 2025'
    },
    {
        'author': '<DevsMentoring>',
        'title': 'What if...',
        'content': "That's my second post>",
        'date': '29 April 2025'
    }
]

def home(request):
    return render(request, 'blog/home.html', {'title': 'Home', 'posts': Article.objects.all()})

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
