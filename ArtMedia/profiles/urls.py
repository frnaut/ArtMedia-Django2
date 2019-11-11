from django.urls import path
from .views import ProfileListView, ProfileDetailView, ProfileDeleteView, ProfileBlock

urlpatterns = [
    path('lista/', ProfileListView.as_view(), name='profile_list'),
    path('<username>/',ProfileDetailView.as_view(), name='profile_details' ),
    path('eliminar/<int:<pk>', ProfileDeleteView.as_view(), name='eliminar-perfil'),
    path('<username>/bloquear/<int:pk>', ProfileBlock.as_view(), name='block-profile')
    
]
