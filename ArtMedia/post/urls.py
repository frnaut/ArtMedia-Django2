from django.urls import path
from .views import PostCreateView, PostDeleteView

urlpatterns = [
    path('', PostCreateView.as_view(), name='post'),
    path('eliminar/<int:pk>', PostDeleteView.as_view(), name='eliminar-post')
]
