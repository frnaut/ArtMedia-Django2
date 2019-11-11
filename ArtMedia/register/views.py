from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile

# Create your views here.
class SignUpClassView(CreateView):

    form_class = UserCreationForm
    template_name = 'registration/singup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignUpClassView, self).get_form()
        # modificar fomulario
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Nombre de usuario'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Repita la contraseña'})
        
        return form


@method_decorator(login_required, name='dispatch')
class UpdateProfile(UpdateView):
    model= Profile
    fields = ['avatar', 'bio', 'link']
    success_url = reverse_lazy('register_profile')
    template_name = 'registration/update_profile.html'

    # modificar formulario
    def get_form(self, form_class=None):
        form = super(UpdateProfile, self).get_form()
        form.fields['avatar'].widget = forms.FileInput(attrs={'class':'form-control-file mb-2'})
        form.fields['bio'].widget = forms.Textarea(attrs={'class':'form-control','row':3, 'placeholder':'Biografia'})
        form.fields['link'].widget = forms.URLInput(attrs={'class':'form-control','placeholder':'Enlace a tu pagina'})
        
        return form
    # recuperar objeto para identificar el usuario logueado
    def get_object(self):
        profile, created =  Profile.objects.get_or_create(user=self.request.user)
        return profile
