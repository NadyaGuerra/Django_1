from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, CreateView, DeleteView
from pytils.translit import slugify
from blog.models import Blog


# Create your views here.
class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'image',)
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)




class BlogListView(ListView):
    model = Blog
    extra_context = {
        'title': 'Блог'
    }
