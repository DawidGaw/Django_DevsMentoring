from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article.html'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'blog/article_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = 'blog/article_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'blog/article_delete.html'
    success_url = '/'

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author


def test_api(request):
    return render(request, 'blog/test_api.html')

