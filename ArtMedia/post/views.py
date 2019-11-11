from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django import forms
from .forms import PostsForm
from .models import Post

# Create your views here.

@method_decorator(login_required, name = 'dispatch')
class PostCreateView(CreateView):
    model = Post
    fields = ['img', 'detail', 'user']
    success_url = reverse_lazy('home')
    template_name = 'post/post.html'

    def get_form(self, form_class=None):
        form = super(PostCreateView, self).get_form()

        form.fields['img'].widget = forms.FileInput(attrs={'class':'form-control-file mb-3'})
        form.fields['detail'].widget = forms.Textarea(attrs={'class':'form-control'})
        form.fields['user'].widget = forms.TextInput(attrs={'class':'form-control d-none','value':self.request.user.id})

        return form

class PostListView(ListView):
    model = Post
    template_name = 'core/home.html'
    ordering = ['-created']
    paginate_by = 10

class PostDeleteView(DeleteView):
    model = Post
    def get_success_url(self):
        return reverse_lazy('home') + '?eliminado'