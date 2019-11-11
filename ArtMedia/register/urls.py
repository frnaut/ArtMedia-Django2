from django.urls import path
from .views import SignUpClassView, UpdateProfile

urlpatterns = [
    path('signup/', SignUpClassView.as_view(), name='signup'),
    path('profile/', UpdateProfile.as_view(), name='register_profile'),
]
