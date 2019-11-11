from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User 
from register.models import Profile

# Create your views here.
class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    paginate_by = 10

class ProfileDetailView(DetailView):
    model = Profile

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])

class ProfileDeleteView(DeleteView):
    model = User
    
    def get_success_url(self):
        return reverse_lazy('profile_list') + '?eliminado'

class ProfileBlock(UpdateView):
    model = Profile
    fields = ['block']
    template_name_suffix = '_block_profile'

    def get_success_url(self):
        return reverse_lazy('profile_list') + '?ok'