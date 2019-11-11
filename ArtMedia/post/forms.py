from django import forms
from .models import Post

# formularios
class PostsForm(forms.Form):
    
    class Meta:
        model = Post
        fields = ['img', 'detail','user']
