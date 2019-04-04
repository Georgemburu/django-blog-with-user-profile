from django.shortcuts import render
from django import http
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
# Create your views here.
class PostListView(ListView):
    model = Post
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args)
        context['title'] = 'Home'
        return context

class PostDetailView(DetailView):
    model = Post
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args)
        context['title'] = 'PostDetails'
        return context


class PostCreateView(CreateView):
    model = Post
    fields = [
        'title',
        'body',
        'image'
    ]
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args)
        context['title'] = 'PostCreate'
        context['heading'] = 'Create Post'
        return context

    def get_success_url(self):
        return reverse_lazy('post_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return http.HttpResponseRedirect(self.get_success_url())

class PostUpdateView(UpdateView):
    model = Post
    fields = [
        'title',
        'body',
        'image'
    ]
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args)
        context['title'] = 'PostEdit'
        context['heading'] = 'Edit Post'

        return context
