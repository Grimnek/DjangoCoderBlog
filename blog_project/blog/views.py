from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post


class BlogListView(ListView):
    paginate_by = 4
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'CRUD/post_detail.html'


class BlogCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'CRUD/post_new.html'
    fields = ['title', 'text']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'CRUD/post_edit.html'
    fields = ['title', 'text']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'CRUD/post_delete.html'
    success_url = reverse_lazy('home')