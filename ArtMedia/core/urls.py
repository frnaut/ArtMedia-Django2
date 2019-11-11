from django.urls import path
from .views import HomeClasView
from post.views import PostListView

urlpatterns = [
    path('',PostListView.as_view(), name='home')    
]
 