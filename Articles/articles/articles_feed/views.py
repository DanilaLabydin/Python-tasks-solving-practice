from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .forms import *
from .models import *
from django.views.generic import ListView, DetailView, CreateView
from .utils import *


class ArticlesHome(DataMixin, ListView):
    model = Article
    template_name = 'articles_feed/index.html'
    context_object_name = 'articles'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Main page')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Article.objects.filter(is_published=True)


def about(request):
    return render(request, 'articles_feed/about.html', {'title': 'about us'})


class AddArticle(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddArticleForm
    template_name = 'articles_feed/new_article.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Add article')
        return dict(list(context.items()) + list(c_def.items()))


def login(request):
    return HttpResponse('Log in')


def contacts(request):
    return HttpResponse('contacts')


class ShowArticle(DataMixin, DetailView):
    model = Article
    template_name = 'articles_feed/article.html'
    slug_url_kwarg = 'article_slug'
    context_object_name = 'article'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['article'])
        return dict(list(context.items()) + list(c_def.items()))


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


class ArticleCategory(DataMixin, ListView):
    model = Article
    template_name = 'articles_feed/index.html'
    context_object_name = 'articles'
    allow_empty = False

    def get_queryset(self):
        return Article.objects.filter(cat__slug=self.kwargs['cat_slug'],
                                      is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Category - ' + str(context['articles'][0].cat),
                                      cat_selected=context['articles'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'articles_feed/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Sign in')
        return dict(list(context.items()) + list(c_def.items()))